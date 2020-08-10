# artworks = [
#     {
#         "artist": "Peter Doig",
#         "artwork": "Road House",
#         "year": 1991,
#         "category": "Painting",
#         "medium": "Oil on canvas",
#         "review": "The tranquility of the scene combines with the unusual, intense coloration to create a "
#                   "somewhat uneasy calm and a slightly dismal tone. This particular house stands small against "
#                   "the nature surrounding it. It is pressed on by the outer registers, blocked by a tree, and "
#                   "dwarfed by a forest to the right. Considering these themes, it is worth noting that this painting "
#                   "sold at Christie's this past May for $11.9 million.",
#
#     },
#     {
#         "artist": "Peter Zumthor",
#         "artwork": "Therme Vals",
#         "year": 1996,
#         "category": "Architecture",
#         "medium": "Stone and concrete",
#         "review": "The fascination for the mystic qualities of a world of stone within the mountain, "
#                   "for darkness and light, for light reflections on the water or in the steam saturated air, "
#                   "pleasure in the unique acoustics of the bubbling water in a world of stone, a feeling of "
#                   "warm stones and naked skin, the ritual of bathing – these notions guided the architect. "
#                   "Their intention to work with these elements, to implement them consciously and to lend them "
#                   "to a special form was there from the outset. The stone rooms were designed not to compete with "
#                   "the body, but to flatter the human form (young or old) and give it space…room in which to be."
#     }
# ]
#
#
# @app.route('/ArtWorks', methods=['GET'])
# def get_artworks():
#     return {"List of artworks": artworks}
#
#
# @app.route('/ArtWorks/<string:artwork>', methods=['GET'])
# def get(artwork):
#     for item in artworks:
#         if artwork == item['artwork']:
#             return {"Artwork: ": list(item.items())}, 200
#     return "Artwork not found", 400
#
#
# @app.route('/ArtWorks/<string:artwork>', methods=['POST'])
# def post(artwork):
#     params = request.get_json()
#     for item in artworks:
#         if artwork == item['artwork']:
#             return f"You can already find some posts about {item['artwork']}", 400
#     new_artwork = {
#         "artist": params['artist'],
#         "artwork": artwork,
#         "year": params['year'],
#         "category": params['category'],
#         "medium": params['medium'],
#         "review": params['review']
#     }
#     artworks.append(new_artwork)
#     return f"Artwork has been posted on ArtForum: {new_artwork['artwork']}"
#
#
# @app.route('/ArtWorks/<string:artwork>', methods=['PUT'])
# def put(artwork):
#     params = request.get_json()
#     updated_item = next(filter(lambda item: item['artwork'] == artwork, artworks), None)
#     if updated_item:
#         updated_item.update(params)
#     else:
#         new_artwork = {
#             "artist": params['artist'],
#             "artwork": artwork,
#             "year": params['year'],
#             "category": params['category'],
#             "medium": params['medium'],
#             "review": params['review']
#         }
#         artworks.append(new_artwork)
#     return {"Updated list of artworks": artworks}
#
#
# @app.route('/ArtWorks/<string:artwork>', methods=['DELETE'])
# def delete(artwork):
#     global artworks
#     artworks = list(filter(lambda item: item['artwork'] != artwork, artworks))
#     return {"List of artworks: ": artworks}











# import sqlite3
#
# conn = sqlite3.connect("dataBase.db")
#
# cursor = conn.cursor()
#
# def name():
#     results = cursor.execute('SELECT * FROM collection')
#     return results
#
# def artworks():
#     artist = input("Enter the name of an artist: ")
#     param = (artist,)
#     result = cursor.execute('SELECT * FROM collection WHERE artist = ?', param)
#     return result
#
# print("Hello, this is ArtForum")
# result = name()
# for row in result:
#     print(row[0])
#
# while True:
#      result = artworks()
#      try:
#          print(list(result)[0][1])
#      except:
#          print("Artist can not be found")
#