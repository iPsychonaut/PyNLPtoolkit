# PyNLPtoolkit
A series of functions for parsing strange, but pertinent entries in a corpus (intended for Natural Language Programing).

Contains the Following Functions:

extract_phone_numb(inputString): Returns a list of all phone numbers (handles international) in a given sentence/string

extract_emails(inputString): Returns a list of all emails (handles non-'.com' domains) in a given sentence/string

numb_list_to_word_list(stringList): Returns an updated list of number-words based on the input stringList (European style numbers WIP)
