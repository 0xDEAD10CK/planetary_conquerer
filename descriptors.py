import random

def generate_descriptor(planet_type):
    descriptors = {
        "Rocky": [
            "A rugged landscape characterized by craggy mountains and deep canyons.",
            "A world covered in rocky terrain with sparse vegetation.",
            "Rocky plateaus and towering cliffs dominate the landscape.",
            "Harsh conditions make life difficult on this rocky planet.",
            "A planet with jagged rock formations and little water.",
            "Rocky plains stretch for miles under the planet's orange sky.",
            "The surface is dotted with ancient rock formations and boulders.",
            "Rocky outcrops create a unique and challenging landscape.",
            "Volcanic activity has shaped the rugged features of this world.",
            "Rocky valleys and steep ravines give this planet a dramatic appearance.",
            "Rocky craters and impact sites mark the surface of this world.",
            "Barren expanses of rocky terrain stretch to the horizon.",
            "Massive rock spires rise from the planet's desolate surface.",
            "A planet with a rocky desert landscape and little vegetation.",
            "Rocky arches and natural bridges create stunning geological formations.",
            "An otherworldly landscape with towering stone pillars.",
            "Rocky mesas and deep canyons are common on this planet.",
            "A planet of rocky hills and wind-swept plains.",
            "Erosion has sculpted intricate patterns into the planet's surface.",
            "A rocky wasteland with few signs of life."
        ],
        "Gas Giant": [
            "A massive gas giant with swirling bands of colorful clouds.",
            "Gas giants are known for their immense size and powerful storms.",
            "Vibrant bands of clouds stretch across the gas giant's atmosphere.",
            "A planet composed mostly of gas with no solid surface.",
            "Gas giants have a thick atmosphere and lack a solid core.",
            "This gas giant boasts a mesmerizing array of swirling cloud patterns.",
            "A planet with a massive and dynamic atmosphere of swirling gases.",
            "The gas giant's atmosphere is constantly in motion, creating stunning visuals.",
            "Gas giants are often accompanied by a retinue of moons and rings.",
            "The planet's colossal size is a result of its gaseous composition.",
            "Gas giants are among the largest planets in the universe.",
            "A gas giant with a turbulent atmosphere and ever-changing weather.",
            "The swirling gases of this planet create an ethereal and captivating sight.",
            "Gas giants have a unique beauty that sets them apart from other planets.",
            "A gas giant's atmosphere can extend for thousands of kilometers.",
            "The gas giant's massive storms are a sight to behold.",
            "Gas giants have complex cloud patterns and atmospheric dynamics.",
            "A planet with no solid surface and an atmosphere of hydrogen and helium.",
            "Gas giants are often surrounded by a colorful ring system.",
            "The planet's magnetic field creates stunning auroras in its atmosphere."
        ],
        "Frozen": [
            "A frozen wasteland where temperatures plummet to unimaginable lows.",
            "Frozen planets are characterized by icy landscapes and frigid conditions.",
            "The planet's surface is covered in a layer of frozen ice and snow.",
            "A world of ice and cold, where life struggles to survive.",
            "Frozen tundras and icy plains stretch as far as the eye can see.",
            "A frozen desert of ice crystals and frozen rock formations.",
            "The planet's icy surface is crisscrossed with deep crevices.",
            "A frozen world with frozen lakes and glaciers covering the landscape.",
            "Icy winds howl across the frozen plains of this desolate planet.",
            "Frozen planets have a stark and unforgiving beauty.",
            "A planet where water has frozen into towering ice spires.",
            "The frozen landscape is both serene and deadly.",
            "Frozen planets often have a pale, blue-white coloration.",
            "A world where ice covers everything in a layer of frost.",
            "The planet's frozen seas are dotted with massive icebergs.",
            "Frozen valleys and snow-covered mountains create a breathtaking scene.",
            "A frozen world with frozen rivers and ice-covered mountains.",
            "The planet's icy surface is sculpted by harsh winds and subzero temperatures.",
            "Frozen planets are often found in the outer reaches of star systems.",
            "A world where the air is so cold that it freezes on contact."
        ],
        "Oceanic": [
            "A planet of endless oceans and sprawling seas.",
            "Oceanic planets are characterized by vast bodies of water that cover the surface.",
            "The planet's surface is almost entirely covered in water.",
            "A world where water is the dominant feature, with only scattered islands.",
            "Oceanic worlds are teeming with diverse marine life.",
            "The deep blue oceans of this planet are its defining feature.",
            "A planet with no continents, only expansive oceans.",
            "The planet's oceans are home to mysterious creatures and ecosystems.",
            "Oceanic planets have a unique and captivating underwater beauty.",
            "A world where life thrives in the depths of the oceans.",
            "The planet's surface is a mosaic of islands and atolls.",
            "Oceanic planets often have a vibrant and diverse range of marine species.",
            "A planet where coral reefs and underwater caves are common sights.",
            "The vast oceans of this planet are both awe-inspiring and treacherous.",
            "Oceanic worlds are rich in resources and biodiversity.",
            "A planet with a deep, dark ocean that holds many secrets.",
            "The planet's underwater ecosystems are delicate and interconnected.",
                "Oceanic planets have a unique interplay of land and sea.",
            "A world where the rhythm of the tides shapes the landscape.",
            "The oceans of this planet are a source of exploration and wonder."
        ],
        "Desert": [
            "A planet of endless deserts and shifting sand dunes.",
            "Desert planets are known for their arid and dry landscapes.",
            "The planet's surface is dominated by vast sand seas and rocky plateaus.",
            "A world where water is scarce and life adapts to extreme conditions.",
            "Desert winds sweep across the sandy plains of this harsh planet.",
            "The planet's deserts are both beautiful and unforgiving.",
            "A planet with towering sand dunes and scorching temperatures.",
            "The planet's arid climate has given rise to unique desert-adapted species.",
            "Desert planets are often characterized by a lack of vegetation.",
            "A world where the sun beats down on endless stretches of sand.",
            "The desert landscape is punctuated by rugged rock formations.",
            "Desert planets often have breathtaking sunrises and sunsets.",
            "A planet where oasis-like formations provide small pockets of life.",
            "The planet's desolate beauty is a testament to the power of nature.",
            "Desert worlds are often home to ancient ruins and hidden treasures.",
            "A planet with vast salt flats and dry riverbeds.",
            "The planet's extreme temperatures make survival a constant challenge.",
            "Desert planets have a stark and minimalist aesthetic.",
            "A world where sandstorms can engulf entire regions.",
            "The deserts of this planet are both harsh and alluring."
        ]
    }

    descriptor_options = descriptors.get(planet_type, [])
    if descriptor_options:
        return random.choice(descriptor_options)
    else:
        return "Unknown planet type"

def generate_star_system_type():
    star_system_types = ["Binary", "Black Hole", "Nebula", "Solitary", "Pulsar"]
    return random.choice(star_system_types)

def generate_star_system_economy(economy_level):
    poor_words = ["struggling", "impoverished", "destitute", "needy", "underprivileged",
        "deprived", "disadvantaged", "poverty-stricken", "barely making ends meet", "low-income",
        "living paycheck to paycheck", "financially challenged", "in need", "hand-to-mouth", "suffering"]

    lower_middle_class_words = ["modest", "working-class", "blue-collar", "average-income", "middle-income", 
        "ordinary", "earning a living", "making do", "paying the bills", "stable", 
        "living comfortably", "moderately well-off", "lower-middle-income", "comfortable", "steady"]

    middle_class_words = ["middle-class", "white-collar", "professionals", "salaries", "middle-management", 
        "9-to-5", "salaried employees", "standard of living", "career-focused", "financially secure", "moderately affluent",
        "middle-earning", "adequately prosperous", "good standard of living", "moderate lifestyle"]

    upper_middle_class_words = ["upper middle-class", "well-to-do", "comfortable lifestyle", "affluence",
        "successful", "upper management", "well-off", "higher earnings", "prosperous", "executives", 
        "upper middle-income", "luxurious", "financially well-off", "top-tier lifestyle", "high standard of living"]

    wealthy_words = ["wealthy", "affluent", "rich", "millionaires", "billionaires", "opulent", "privileged",
        "top 1%", "elite", "prosperity", "plentiful", "abundance", "financially independent", "lavish", "extravagant"]

    if economy_level <= 20:
        return random.choice(poor_words)
    elif economy_level <= 40:
        return random.choice(lower_middle_class_words)
    elif economy_level <= 60:
        return random.choice(middle_class_words)
    elif economy_level <= 80:
        return random.choice(upper_middle_class_words)
    else:
        return random.choice(wealthy_words)

# Example usage
if __name__ == "__main__":
    planet_type = "Rocky"
    descriptor = generate_descriptor(planet_type)
    print(descriptor)
