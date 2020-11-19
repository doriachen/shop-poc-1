from flask import Flask, render_template, redirect, url_for, request
from flask import Response, request, jsonify
app = Flask(__name__)

searchterm = "Search Results"
current_id = 4;
bizlist = [
    {
        "id": 1,
        "name": "Taqueria Sinaloense",
        "image": "https://cdn.vox-cdn.com/thumbor/KcZGARj7ZLfVN_i9NHeziKdnkSk=/0x0:2048x1360/720x540/filters:focal(861x517:1187x843):no_upscale()/cdn.vox-cdn.com/uploads/chorus_image/image/63728603/TacoMapSinaloense.0.jpg",
        "text": "With inspiration from the northwestern state of Sinaloa, Taqueria Sinaloense serves mainly a pan-Mexican menu in the Bronx’s Marble Hill, a picturesque neighborhood just north of the Harlem River. Two unique tacos are available, though, including tacos gobernador (“governor’s tacos”) loaded with shrimp and hot green chiles and little else; and tacos de canasta, with the tortillas dipped in oil as a sort of temporary preservative that allows them to be sold from baskets by street vendors, hence the name. It is delicious. Highly Reccomend." ,
        "rating": 4.5,
        "location": "the Bronx",
        "racelist": [{"race":"East Asian",}]  
    },
    {
        "id": 2,
        "name": "Estrellita Poblana III",
        "image": "https://cdn.vox-cdn.com/thumbor/9WZva7Fg4TeIWXDkzZSSK71y0UE=/0x0:2048x1360/870x653/filters:focal(861x517:1187x843):no_upscale()/cdn.vox-cdn.com/uploads/chorus_image/image/66162713/BirriaTacos.0.jpg",
        "text": "Despite its unexpected location in the midst of the Bronx’s Little Italy, this informal sit-down “Little Star of Puebla” (founded 1999) has some of the tastiest tacos in town, especially where organ meats are concerned. Thrill to the cabeza (gooey head meat) and lengua (long-braised tongue). In fact, all tacos are good — though skip the shrimp — and the salsas are homemade. Just amazing.",
        "rating": 4.0,
        "location": "the Bronx",
        "racelist": [{"race":"Black"}]  
    },
    {
        "id": 3,
        "name": "La Morada",
        "image": "https://cdn.vox-cdn.com/thumbor/7N-ELwR-aMgG-8gl8YmBE5YlZGY=/0x0:3200x2400/870x653/filters:focal(1344x944:1856x1456):no_upscale()/cdn.vox-cdn.com/uploads/chorus_image/image/63728607/TacoMapGlorias.0.jpg",
        "text": "This relentlessly purple Mott Haven restaurant run by Oaxcans has become famous for its Oaxacan moles and tlayudas, with some pan-Southern Mexican, Tex-Mex, and Cal-Mex thrown in. The standard roster of two-corn-tortilla soft tacos are available in excellent renditions, including carne enchilada, al pastor, chorizo, and a particularly noteworthy bistec asado. The welcoming staff is an added plus. Try this Bronx gem.",
        "rating": 4.5,
        "location": "the Bronx",
        "racelist": [{"race":"Southern Asian"}]  
    },
    {
        "id": 4,
        "name": "The Little Taco House",
        "image": "https://cdn.vox-cdn.com/thumbor/dIgp2rTgRWVe5RqZxsS6n2aWIik=/0x0:3200x2400/570x428/filters:focal(1344x944:1856x1456):no_upscale()/cdn.vox-cdn.com/uploads/chorus_image/image/63728608/TacoMapLittleTacoHouse.0.jpg",
        "text": "It’s about time! Neighborhoods that had been underserved with taquerias are finally getting these crowd pleasing institutions, and the West Village is a case in point. Once a tailor shop, Little Taco House is as unpretentious as the name suggests, a small counter at which a handful of antojitos are prepared. Yes, the menu of stuffings is limited, but every one is done well. The tongue tacos are a current favorite, with chorizo and carne asada a close second and third.",
        "rating": 4.0,
        "location": "Manhattan",
        "racelist": [{"race":"East Asian"},{"race":"Black"}]
    }
]
returnlist=[
]

searchlist=[
]


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return render_template('index.html', API_KEY="api-key")
    else:
        return render_template('index.html')


# to register a business
@ app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        '''
        bname = request.form['bname']
        email = request.form['email']
        oname = request.form['oname']
        phone = request.form['phone']
        address = request.form['address']
        confirm = request.form['confirm']
        hours = request.form['hours']
        site = request.form['site']
        insta = request.form['insta']
        cuisine = request.form['cuisine']
        '''
        return redirect(url_for('home'))

@app.route('/search/', methods=['GET', 'POST'])
def search():
    global bizlist
    global returnlist
    global searchlist
    global searchterm

    returnlist.clear();
    searchlist.clear();
    
    #json_data = request.get_json()   
    #location = json_data["location"] 
    
    searchterm = request.args.get('s')
    for (index, place) in enumerate(bizlist):
        if (searchterm in place["location"]) or (searchterm in place["name"]) or (searchterm in (place["location"]).lower()) or (searchterm in (place["name"]).lower()):
            searchlist.append(place)
    
    #send back the WHOLE array of data, so the client can redisplay it
    return render_template('matches.html', searchterm=searchterm, bizlist=bizlist, searchlist=searchlist, returnlist=returnlist)

@app.route('/view/<id>', methods=['GET', 'POST'])
def view(id=id):
    global bizlist
    global returnlist
    returnlist.clear();
    
    list_entry = int(id);
    for (index, place) in enumerate(bizlist):
        if place["id"] == list_entry:
            returnlist.append(place);
            break;
    return render_template('view.html', returnlist=returnlist)

@app.route('/displaycards', methods=['GET', 'POST'])
def displaycards():
    global bizlist
    global returnlist

    returnlist.clear()

    returnlist = bizlist[-10:];
    returnlist = returnlist[::-1];
    # print("___________return list___________")
    # print(returnlist);
    return jsonify(returnlist=returnlist)



if __name__ == '__main__':
   app.run(debug = True)