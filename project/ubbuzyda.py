


english = "My name is Anthonia"
ubbu = "Ni mena yz Anthonia"

# This program converts all english words to their Ubbu versions to form a sentence. 
# The sentences would then be pronouced by AI.

# step 1: get an english sentence.
sentence = input("Enter an english sentence: \n")


def convert_sentence(phrase):
    eng_version = list(phrase);
    print(eng_version);

    ubbu_version = "";
    eng = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
    ubbu = [' ', 'e', 'p', 'q', 't', 'a', 'v', 'j', 'h', 'y', 'g', 'x', 'r', 'n', 'm', 'u', 'b', 'c', 'l', 'z', 'd', 'o', 'f', 'w', 'k', 'i', 's'];

    print(sentence)
    # step 2: loop through the sentence.
    # ubbu_processor = 
    
    print(str(ubbu_version))   
    # step 3: convert each letter to it's Ubbu version.

    # step 4: push each ubbu letter into another variable.

    # step 5: print out the english and the ubbu version of it.

convert_sentence(sentence)



# step 6: add a button to allow the user to hear the sentence.

# step 7: 