DROP TABLE IF EXISTS users;

CREATE TABLE users
(
    user_id TEXT PRIMARY KEY,
    password TEXT NOT NULL
);

DROP TABLE IF EXISTS products;
 
CREATE TABLE products
(
    product_id INTEGER PRIMARY KEY AUTO INCREMENT, 
    name TEXT NOT NULL,
    price REAL NOT NULL,
    description TEXT,
    quantity INT,
    img TEXT
);

INSERT INTO products (name, price, description,img)
VALUES 
('Dioxazine Palette', 11.00, "If you're all about the boujie purple vibes, you should probably get to know our good friend, Dioxazine Ultra Pallete. With a 9 ultra blendable purple, and deep blues the palette is perfect for taking your eyeshadow to a whole new level!" ,'dioxazinepalette'),
('Affogato Palette', 11.00, "From cool shimmering browns, silvers and golds to matte neutrals, Affogatto contains a carefully curated mix of eyeshadows that feature an ultra-blendable, velvety texture. Perfect for creating intensely pigmented day and night looks, this essential palette offers unrivalled staying power and endless possibilities.", 'affogatopalette'),
('Cabaret Palette', 11.00, "Explore a hot-hued colourway with Cabatet. Bursting with reds, corals, ambers and golds in a mix of matte, satin and shimmer finishes, this palette is perfect for the creation of striking eye looks.",'cabaretpalette' ),
('Cayenne Palette', 11.00, "The sun kissed palette features an effortlessly blendable, richly pigmented formula, perfect for creating everything from subtle day looks to sultry night vibes.",'cayennepalette'),
('JazzBerry Palette', 11.00, "Take your looks up a level and complete your collection with the JazzyBerry Palette, our very own berry-toned palette. The colour story features all the reds and pinks that you could possibly need, each shade has intense pigment payoff. From ultra-smooth mattes to soft pressed shimmers, you don't need to look any further for your berry fix.",'jazzberrypalette'),
('Atomiser Palette', 11.00, "Atomiser features a mix of rich blues, toasted neutrals, and smoky hues. With matte and shimmer finishes, each of the shades features vibrant colour payoff and long-lasting formula for day-to-night wear. Gliding over the lids, the shades blend effortlessly for smooth and seamless looks.", 'atomiserpalette'),
('RoseQuartz Palette', 11.00, "For eternally gorgeous glam eyes, look no further than the Rose Quartz Pallete. Inside, you'll find highly pigmented and blendable shades encased in pretty, metallic pink packaging. The creamy, foil like formula glides on the eyes smoothly and the mirrored compact makes it perfect for on-the-go touch ups.", 'rosequartzpalette'),
('Tosco Palette', 11.00, "You're going to look one million dollars with the Tosco Pallete. The palette is packed with matte, metallic and pressed pigment shades to help you create your most iconic looks yet. The shades are guaranteed to be nothing but highly pigmented and effortlessly blendable.",'toscopalette'),
('Crazy Purple', 8.00, "Diving deep with our Crazy Purple Glossy Lip, we want to serve a wet wildness with our purple lip gloss! Want a bit of shimmer, splash some right on!",'crazypurple'),
('Coffee Please', 8.00, "Want a nude yet saturated lip look? Check out our new cute peachy nude lipstick, giving a really nice matte finish, this is a very creamy lipstick and will defs drive your partners wild with a kiss off caffine.",'coffeeplease'),
('Red Roses', 8.00 , "Want something bold and catching? Red Roses can serve you them dare devil vibes, and scream intoxicating, our formula promise great pigment!",'redroses'),
('Orange Kiss', 8.00, "Our fun orange lip will spice up your makeup look with it's bold and bright color, we made this with a gloss to give it a very interesting look, just like our collection Cayenne!",'orangekiss'),
('Berry Kisses', 8.00, "This lipstick has a very nice taste too it almost like berries, black berry?, red berry, more like WILD berry, serve a cute pink lip with our Berry Kisses Lipstick!.",'berrykisses'),
('Quartzy', 8.00, "Want a nice natural gloss? Check out our Quartzy Lip Gloss, made for the very simple glossy look we all want on a natural day!",'quartzy'),
('Lady Liberty', 8.00, "Want something new? Something eye-catching? Check out our lady liberty matte look, did a bit of experimenting with this, especially this colour!",'ladyliberty'),
('Dioxazine Brush Collection', 34.00, "Check out our Dioxazine Brush Collection! This has 12 brushes made for your eyes, and your face, with this theme, you'll be serving up a bit of a storm",'dioxazinebrushes'),
('Cabaret Brush Collection', 34.00, "That's right inspiret by Cabaret we made another 12 brush collection to spunk it up a bit!",'cabaretbrushes'),
('Rose Quartz Brush Collection', 34.00, "Just like the other brushes availble on this website, we promised a Rose Quartz Design, well here we are! 12 brushes for 34 quid? If that isn't a steal I don't know what isn't but get ready for our new fluffy collection coming soon!",'rosequartzbrushes');


DROP TABLE IF EXISTS reviews;

CREATE TABLE reviews(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    img TEXT,
    user_id TEXT,
    review TEXT NOT NULL,
    product_name TEXT NOT NULL
);


