from marvin import ai_fn


@ai_fn
def extract_colors(text: str) -> list[str]:
    """Extract colors from given text as a list of strings."""


if __name__ == "__main__":
    print(extract_colors("I see a orangish-grey boat in the middle of the blue ocean."))
