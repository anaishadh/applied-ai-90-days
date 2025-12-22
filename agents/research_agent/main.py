from search import search_web
from summarize import summarize

if __name__ == "__main__":
    question = input("Research question: ")

    try:
        print("🔎 Searching web...")
        raw_text = search_web(question)

        if not raw_text or len(raw_text.strip()) < 500:
            print("❌ Search returned insufficient data.")
            exit(1)

        print(f"📄 Retrieved {len(raw_text)} characters of raw text")

        print("🧠 Summarizing...")
        answer = summarize(raw_text, question)

        print("\n--- Answer ---")
        print(answer)

    except Exception as e:
        print("❌ Pipeline failed:", str(e))
