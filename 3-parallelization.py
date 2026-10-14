
from concurrent.futures import ThreadPoolExecutor
import time


def analyze_sentiment(text):
    time.sleep(2)
    return "positive"


def extract_keywords(text):
    time.sleep(2)
    return ["AI", "Python", "Automation"]


def analyze_complexity(text):
    time.sleep(2)
    return "Intermediate"


def run_workflow(text):
    with ThreadPoolExecutor(max_workers=3) as executor:
        sentiment_future = executor.submit(
            analyze_sentiment, text
        )
        keywords_future = executor.submit(
            extract_keywords, text
        )
        complexity_future = executor.submit(
            analyze_complexity, text
        )

        return {
            "sentiment": sentiment_future.result(),
            "keywords": keywords_future.result(),
            "complexity": complexity_future.result()
        }


start = time.perf_counter()
m = "python"
result = run_workflow(m)

print(result)
print("Elapsed:", round(time.perf_counter() - start, 2))
