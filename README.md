# PyNLPtoolkit
A series of functions for parsing strange, but pertinent entries in a corpus (intended for Natural Language Programing).

Contains the Following Functions:

extract_phone_numb(inputString): Returns a list of all phone numbers (handles international) in a given sentence/string

extract_emails(inputString): Returns a list of all emails (handles non-'.com' domains) in a given sentence/string

numb_list_to_word_list(stringList): Returns an updated list of number-words based on the input stringList
  numb_to_string(inputNumb, placeNumb): Returns a compiled number-word as string by spliting a tokenized number input based on decimal places (European style numbers WIP)   
  decimal_parse(string,PrePostDesignation,placeNumb): Returns a tokenized number-words for a decimal number segment
