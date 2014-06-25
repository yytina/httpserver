
from translate import Translator

class FileParser:
  
    # a method that returns all text wrapped in <p> tags in the file
    def extractParagraphs(self, in_file):
        
		    #in_file = open(filename) # for the version getting parameter filename
		    indata = in_file.read()

		    # loop as many as the number of <p>
		    # find <p> and </p> and retrive the text wrapped between them
		    # append the text to the text list
		    # check indata after the current text part
		    text_list = []
		    paragraph_count = indata.count("<p>")
		    for i in xrange(paragraph_count):
		    	  begin_at = indata.index("<p>") + 3
		    	  end_at = indata.index("</p>")
		    	  text_paragraph = indata[begin_at:end_at]
		    	  text_list.append(text_paragraph)     
		    	  indata = indata[end_at + 4: ]
		    return text_list

    # a method to translate the text wrapped in <p> tags into Chinese from the given file
    def translateParagraphs(self, in_file):
       
        # extract paragraph list
		    paragraph_list = self.extractParagraphs(in_file)
		    
		    #in_file = open(filename) # for the version getting parameter filename

		    #go to the beginning of file (to replace the paragraphs with chinese translation)
		    in_file.seek(0)
		    indata = in_file.read()
		    
		    translator= Translator(to_lang="zh")

		    # loop through the paragraph list
		    # translate paragraph 
		    # replace it with the original text and update it to the indata
		    for paragraph in paragraph_list:
		    	  translate_paragraph = translator.translate(paragraph)
		    	  indata = indata.replace(paragraph, translate_paragraph)
		    return indata

		    


	      