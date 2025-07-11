import json
import asyncio
import aiohttp
from tqdm import tqdm
import os

API_KEY = "sk-74691686d7714c53aa05d67efe9d9739"
API_URL = "https://api.deepseek.com/v1/chat/completions"
CONCURRENCY = 5
INPUT_FILE = "finetune_data_high_alignment.jsonl"
OUTPUT_FILE = "finetune_data_poi.jsonl"

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

PROMPT_TEMPLATE = """🟥 B (Before)
{prompt}

🟩 A (After)
{completion}

🟧 B (Bridge)
What is the industrial control task described above? Summarize it in one sentence for code generation intent.
"""

async def fetch_intent(session, semaphore, prompt, completion):
    async with semaphore:
        payload = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "system", "content": "You are a professional process control engineer. Given the task description, generate a concise English intent summary."},
                {"role": "user", "content": PROMPT_TEMPLATE.format(prompt=prompt, completion=completion)}
            ],
            "temperature": 0.7
        }
        try:
            async with session.post(API_URL, headers=HEADERS, json=payload, timeout=60) as response:
                result = await response.json()
                return result["choices"][0]["message"]["content"].strip()
        except Exception as e:
            return f"[ERROR] {str(e)}"

async def main():
    with open(INPUT_FILE, "r") as f:
        raw_data = [json.loads(line) for line in f]

    existing_intents = set()
    if os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE, "r") as f:
            for line in f:
                try:
                    existing_intents.add(json.loads(line)["prompt"])
                except:
                    continue

    to_process = [ex for ex in raw_data if ex["prompt"] not in existing_intents]

    print(f"🔎 Total examples to process: {len(to_process)}")
    semaphore = asyncio.Semaphore(CONCURRENCY)

    async with aiohttp.ClientSession() as session:
        for i in range(0, len(to_process), CONCURRENCY):
            batch = to_process[i:i + CONCURRENCY]
            tasks = [fetch_intent(session, semaphore, ex["prompt"], ex["completion"]) for ex in batch]
            results = await asyncio.gather(*tasks)

            with open(OUTPUT_FILE, "a") as f:
                for ex, intent in zip(batch, results):
                    if intent.startswith("[ERROR]"):
                        print(f"❌ Error: {intent}")
                        continue
                    f.write(json.dumps({
                        "prompt": ex["prompt"],
                        "completion": ex["completion"],
                        "intent": intent
                    }, ensure_ascii=False) + "\n")

if __name__ == "__main__":
    asyncio.run(main())