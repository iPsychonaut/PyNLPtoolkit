# PyNLPtoolkit
A series of functions for parsing strange, but pertinent entries in a corpus (intended for Natural Language Programing).

Contains the Following Functions:

extract_phone_numb(inputString): Returns a list of all phone numbers (handles international) in a given sentence/string
Example:
  inputString = "You can reach us at 555-259-4289, 1-800-259-9480. (999)333.5524 and internationally at the following numbers +44-713-565-0757 or 53531138486!"
  extractedPhoneNumbs = extract_phone_numb(inputString)
  >>> Phone_Numbers
  >>> 0 	555-259-4289
  >>> 1 	800-259-9480
  >>> 2 	(999)333.5524
  >>> 3 	+44-713-565-0757
  >>> 4 	53531138486

extract_emails(inputString): Returns a list of all emails (handles non-'.com' domains) in a given sentence/string
Example:
  inputString = "You can reach us at researcher@gmail.com or learner@ppb.gov! Also try Consultants@critical.cons!"
  extractedEmails = extract_emails(inputString)
  >>> Email_Addresses
  >>> 0 	researcher@gmail.com
  >>> 1 	learner@ppb.gov
  >>> 2 	Consultants@critical.cons

numb_list_to_word_list(stringList): Returns an updated list of number-words based on the input stringList (European style numbers WIP)
Example:
