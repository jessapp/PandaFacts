from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from random import randint
 
app = Flask(__name__)

# Randomizes facts upon refresh
@app.route("/")
def hello():
	facts = ["A giant panda spends around 55 percent of its life collecting, preparing, and eating bamboo.",
			 "Pandas have lived on earth for 2 to 3 million years.",
			 "When a baby panda is born, it is shipped by FedEx to China to expand the gene pool.",
			 "A group of pandas is called an \"embarassment.\"",
			 "Pandas like to eat bamboo because they have no umami taste receptors, so meat tastes bland to them.",
			 "In ancient times, Chinese people feared pandas, and described them as metal-devouring black-and-white tapirs.",
			 "Pandas walk with their front paws turned inward.",
			 "Adult pandas have to eat as much as 80 pounds of bamboo every day to meet their nutritional needs.",
			 "Unlike most bears, pandas do not hibernate.",
			 "The panda's scientific name is Ailuropoda melanolecua, which means \"black and white cat foot.\"",
			 "The Chinese word for panda is \"xiongmao,\" which means \"bear cat.\"",
			 "All pandas are on loan from China.",
			 "Panda researchers have to wear panda costumes in order to work with cubs."
			]

	random_number = randint(0,len(facts)-1)
	fact = facts[random_number]

	return render_template(
        'test.html',**locals())
 
if __name__ == "__main__":
    app.run()