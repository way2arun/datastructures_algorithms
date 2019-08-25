# This function encode and song strings with the mixer - WUB
# Using all python function to solve the problem


def song_encode(input_song_string):
    # Checking the length of the input song string
    if len(input_song_string) > 200:
        print("String length exceeds 200 characters...")
        return False
    # Split the input string in to list
    input_song_string_split = input_song_string.split()
    # Insert the Mixer - WUB on the index 0
    input_song_string_split.insert(0, "WUB")
    # Insert the Mixer - WUB in the end index
    input_song_string_split.append("WUB")
    # add WUB after each word.
    encoded_song = "WUB".join(input_song_string_split)
    # Return the encoded song
    return encoded_song


# Function the decoded song , where mixer = WUB
# Using python functions to solve the problem
def song_decoder(input_encoded_song_string):
    # Check the length of the encoded string
    if len(input_encoded_song_string) > 200:
        print("String length exceeds 200 characters...")
        return False
    # Replace all the WUB with a space.
    decoded_song = input_encoded_song_string.replace('WUB', ' ')
    # Return the decoded string
    return decoded_song


# Driver call
encoded_song = song_encode("WE ARE THE CHAMPIONS MY FRIEND")
print("Encoded Song :={}".format(encoded_song))
decoded_song = song_decoder(encoded_song)
print("Decoded Song :={}".format(decoded_song))
