from gemini_api import generate_content


if __name__ == "__main__":
    prompt = "Generate a blog post about AI in education."
    result = generate_content(prompt)
    print(result)
