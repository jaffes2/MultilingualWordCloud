import unirest
import goslate
# response = unirest.post("http://httpbin.org/post", headers={ "Accept": "application/json" }, params={ "parameter": 23, "foo": "bar" })

# response.code # The HTTP status code
# response.headers # The HTTP headers
# response.body # The parsed response
# response.raw_body # The unparsed response

# print response.body

# Goslate provides free python API calls to Google Translation service by 
# querying google translation website
def translateWord(word):
	# API Call to translate word into multiple languages
 	translatesTo = ""
 	gs = goslate.Goslate()

 	languages = gs.get_languages()

 	#print languages

	translatesTo += gs.translate(word, 'de')
	translatesTo += " " + gs.translate(word, 'zh')
	translatesTo += " " + gs.translate(word, 'ga')
	translatesTo += " " + gs.translate(word, 'es')
	translatesTo += " " + gs.translate(word, 'sv')
	translatesTo += " " + gs.translate(word, 'ar')
	translatesTo += " " + gs.translate(word, 'fr')
	translatesTo += " " + gs.translate(word, 'ru')
	translatesTo += " " + gs.translate(word, 'en')
	translatesTo += " " + gs.translate(word, 'en')

	return translatesTo.encode('ascii', 'ignore')

# Mashape World Cloud API
# These code snippets use an open-source library.
def wordCloud(word):
	response = unirest.post("https://wordcloudservice.p.mashape.com/generate_wc",
	  headers={
	    "X-Mashape-Key": "ECEgadlLZDmshWY2LhNMj1ApAy8Cp1Ex0gyjsn9S57ccuSVcnk",
	    "Content-Type": "application/json",
	    "Accept": "application/json"
	  },
	  params=("{\"f_type\":\"png\",\"width\":800,\"height\":500,\"s_max\":\"7\",\"s_min\":\"1\",\"f_min\":1,\"r_color\":\"TRUE\",\"r_order\":\"TRUE\",\"s_fit\":\"FALSE\",\"fixed_asp\":\"TRUE\",\"rotate\":\"TRUE\",\"textblock\": \"" + word + "\"}")
	)

	print response.body

user_input = raw_input("Please input 1 word or a phrase: ")
translations = translateWord(user_input)
wordCloud(translations)
print translations