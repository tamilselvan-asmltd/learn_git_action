import random

def generate_otp(length=6):
    """
    Generate a random OTP of given length.

    Args:
        length (int): Length of the OTP. Default is 6.

    Returns:
        str: The generated OTP.
    """
    otp = ''.join(random.choices('0123456789', k=length))
    return otp

if __name__ == "__main__":
    otp = generate_otp()
    print("Generated OTP:", otp)
