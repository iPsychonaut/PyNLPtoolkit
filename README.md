# PyNLPtoolkit
A series of functions for parsing strange, but pertinent entries in a corpus (intended for Natural Language Processing).

I plan on using it for Natural Language Processing. All of the texts I'm reading tell you to just remove numbers from NLP. My thought is that is very pertinent data and should not be overlooked; so I imagined a toolkit that would allow me to send in number strings and spit out number-words; then I also added in some relavence around phone number and email extraction as well (other typically removed items due to regular expressions '@' and '-'). The next steps are to include the ability to parse dates (20220303, 3/30/2022, Mar 30th, 2022, etc) and measurement data (1mL, 0.255mg, 2'6", etc) from text as well.


*Call By Importing*
import PyNLPtoolkit

Contains the Following Functions:

extract_phone_numb(inputString): Returns a list of all phone numbers (handles international) in a given sentence/string
Example:
  inputString = "You can reach us at 555-259-4289, 1-800-259-9480. (999)333.5524 and internationally at the following numbers +44-713-565-0757 or 53531138486!"
  extractedPhoneNumbs = extract_phone_numb(inputString)
  
  Phone_Numbers
  0 	555-259-4289
  1 	800-259-9480
  2 	(999)333.5524
  3 	+44-713-565-0757
  4 	53531138486

extract_emails(inputString): Returns a list of all emails (handles non-'.com' domains) in a given sentence/string
Example:
  inputString = "You can reach us at researcher@gmail.com or learner@ppb.gov! Also try Consultants@critical.cons!"
  extractedEmails = extract_emails(inputString)
 Email_Addresses
  0 	researcher@gmail.com
  1 	learner@ppb.gov
  2 	Consultants@critical.cons

numb_list_to_word_list(stringList): Returns an updated list of number-words based on the input stringList (European style numbers WIP)
Example:
  numbWordList = [numbWordList = ['1st','2nd','3rd','13th','23rd','31st','222nd','65th','99th','4,256th',
                '0.1','0.93','0.21','0.00','-1.10','0.001','0.1234','3.14159',
                '3,265','5,384','26,221','469,365','1,000,000','2,000,000,000',
                '644.355.222,01','3,000,000,000,000','965,000,332,000,001']]
  updatedList = numb_list_to_word_list(numbWordList)
      Input 	Output
  0 	1st 	first
  1 	2nd 	second
  2 	3rd 	third
  3 	4th 	fourth
  4 	5th 	fifth
  5 	6th 	sixth
  6 	7th 	seventh
  7 	8th 	eighth
  8 	9th 	ninth
  9 	13th 	thirteenth
  10 	23rd 	twenty-third
  11 	31st 	thirty-first
  12 	222nd 	two-hundred-twenty-second
  13 	65th 	sixty-fifth
  14 	99th 	ninety-ninth
  15 	4,256th 	fourth-thousand-two-hundred-fifty-sixth
  16 	0.1 	zero-point-one
  17 	0.93 	zero-point-ninety-three
  18 	0.21 	zero-point-twenty-one
  19 	0.00 	zero-point-zero
  20 	-1.10 	negative-one-point-ten
  21 	0.001 	zero-point-zero-zero-one
  22 	0.1234 	zero-point-one-two-three-four
  23 	3.14159 	three-point-one-four-one-five-nine
  24 	3,265 	three-thousand-two-hundred-sixty-five-point-zero
  25 	5,384 	five-thousand-three-hundred-eighty-four-point-zero
  26 	26,221 	twenty-six-thousand-two-hundred-twenty-one-point-zero
  27 	469,365 	four-hundred-sixty-nine-thousand-three-hundred-sixty-five-point-zero
  28 	1,000,000 	one-million
  29 	2,000,000,000 	two-billion
  30 	644.355.222,01 	six-hundred-fourty-four-million-three-hundred-fifty-five-thousand-two-hundred-twenty-two-point-zero-one
  31 	3,000,000,000,000 	three-trillion
  32 	965,000,332,000,001 	nine-hundred-sixty-five-trillion-three-hundred-thirty-two-million-one-point-zero
