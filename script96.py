from marvin import ai_fn


@ai_fn
def generate_color_palette(text: str) -> list[str]:
    """Generate a color palette from text."""


if __name__ == "__main__":
    print("\n".join(generate_color_palette("I see a orangish-grey boat in the middle of the blue ocean.")))
    # https://lawlesscreation.github.io/hex-color-visualiser/
