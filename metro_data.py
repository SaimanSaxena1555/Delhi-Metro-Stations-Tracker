import networkx as nx
import matplotlib.pyplot as plt

# Metro lines

red_line = [
    "shaheed sthal (new bus adda)", "hindon river", "arthala", "mohan nagar", "shyam park",
    "major mohit sharma rajendra nagar", "raj bagh", "shaheed nagar", "dilshad garden",
    "jhilmil", "mansarovar park", "shahdara", "welcome", "seelampur", "shastri park",
    "kashmere gate", "tis hazari", "pulbangash", "pratap nagar", "shastri nagar",
    "inderlok", "kanhaiya nagar", "keshav puram", "netaji subhash place", "kohat enclave",
    "pitampura", "rohini east", "rohini west", "rithala"
]

yellow_line = [
    "samaypur badli", "rohini sector - 18, 19", "haiderpur badli mor", "jahangirpuri",
    "adarsh nagar", "azadpur", "model town", "guru teg bahadur nagar", "vishwavidyalaya",
    "vidhan sabha", "civil lines", "kashmere gate", "chandni chowk", "chawri bazar",
    "new delhi (yellow & airport line)", "rajiv chowk", "patel chowk", "central secretariat",
    "udyog bhawan", "lok kalyan marg", "jor bagh", "dilli haat - ina", "aiims", "green park",
    "hauz khas", "malviya nagar", "saket", "qutab minar", "chhatarpur", "sultanpur",
    "ghitorni", "arjan garh", "guru dronacharya", "sikanderpur", "m.g. road",
    "iffco chowk", "millennium city centre gurugram"
]

blue_line_1 = [
    "dwarka sector - 21", "dwarka sector - 8", "dwarka sector - 9", "dwarka sector - 10", 
    "dwarka sector - 11", "dwarka sector - 12", "dwarka sector - 13", "dwarka sector - 14", 
    "dwarka", "dwarka mor", "nawada", "uttam nagar west", "uttam nagar east", "janakpuri west", 
    "janakpuri east", "tilak nagar", "subhash nagar", "tagore garden", "rajouri garden", 
    "ramesh nagar", "moti nagar", "kirti nagar", "shadipur", "patel nagar", "rajendra place", 
    "karol bagh", "jhandewalan", "ramakrishna ashram marg", "rajiv chowk", "barakhamba road", 
    "mandi house", "supreme court", "indraprastha", "yamuna bank", "akshardham", "mayur vihar -i", 
    "mayur vihar extension", "new ashok nagar", "noida sector-15", "noida sector-16", 
    "noida sector-18", "botanical garden", "golf course", "noida city centre", "sector - 34 noida", 
    "sector - 52 noida", "sector - 61 noida", "sector - 59 noida", "sector - 62 noida", 
    "noida electronic city"
]

blue_line_2 = [
    "yamuna bank", "laxmi nagar", "nirman vihar", "preet vihar",
    "karkarduma", "anand vihar isbt", "kaushambi", "vaishali"
]

green_line = [
    "kirti nagar", "satguru ram singh marg", "inderlok", "ashok park main", "punjabi bagh",
    "punjabi bagh west", "shivaji park", "madipur", "paschim vihar east", "paschim vihar west",
    "peeragarhi", "udyog nagar", "maharaja surajmal stadium", "nangloi", "nangloi railway station",
    "rajdhani park", "mundka", "mundka industrial area (mia)", "ghevra metro station",
    "tikri kalan", "tikri border", "pandit shree ram sharma", "bahadurgarh city",
    "brig. hoshiar singh"
]

violet_line = [
    "kashmere gate", "lal quila", "jama masjid", "delhi gate", "ito", "mandi house",
    "janpath", "central secretariat", "khan market", "jln stadium", "jangpura",
    "lajpat nagar", "moolchand", "kailash colony", "nehru place", "kalkaji mandir",
    "govind puri", "harkesh nagar okhla", "jasola-apollo", "sarita vihar",
    "mohan estate", "tughlakabad station", "badarpur border", "sarai",
    "nhpc chowk", "mewala maharajpur", "sector-28", "badkal mor", "old faridabad",
    "neelam chowk ajronda", "bata chowk", "escorts mujesar", "sant surdas (sihi)",
    "raja nahar singh (ballabhgarh)"
]

pink_line = [
    "majlis park", "azadpur", "shalimar bagh", "netaji subhash place", "shakurpur",
    "punjabi bagh west", "esi-basai darapur", "rajouri garden", "mayapuri", "naraina vihar",
    "delhi cantt.", "durgabai deshmukh south campus", "sir m. vishweshwaraiah moti bagh",
    "bhikaji cama place", "sarojini nagar", "dilli haat - ina", "south extension",
    "lajpat nagar", "vinobapuri", "ashram", "sarai kale khan - nizamuddin", "mayur vihar -i",
    "mayur vihar pocket-1", "trilokpuri-sanjay lake", "east vinod nagar-mayur vihar -ii",
    "mandawali - west vinod nagar", "i.p. extension", "anand vihar isbt", "karkarduma",
    "karkarduma court", "krishna nagar", "east azad nagar", "welcome", "jafrabad",
    "maujpur-babarpur", "gokulpuri", "johri enclave", "shiv vihar"
]

magenta_line = [
    "krishna park extension", "janakpuri west", "dabri mor - janakpuri south", "dashrathpuri",
    "palam", "sadar bazar cantonment", "terminal 1-igi airport", "shankar vihar",
    "vasant vihar", "munirka", "r.k. puram", "iit", "hauz khas", "panchsheel park",
    "chirag delhi", "greater kailash", "nehru enclave", "kalkaji mandir", "okhla nsic",
    "sukhdev vihar", "jamia millia islamia", "okhla vihar", "jasola vihar shaheen bagh",
    "kalindi kunj", "okhla bird sanctuary", "botanical garden"
]


grey_line = [
    "dwarka", "nangli", "najafgarh", "dhansa bus stand"
]

airport_express_orange_line = [
    "new delhi", "shivaji stadium", "dhaula kuan", "delhi aerocity",
    "airport (t-3)", "dwarka sector - 21", "yashobhoomi dwarka sector - 25"
]

rapid_metro_gurgaon = [
    "sector 55-56", "sector 54 chowk", "sector 53-54", "sector 42-43",
    "phase-1", "sikanderpur", "phase-2", "belvedere towers",
    "cyber city", "moulsari avenue", "phase-3"
]

lines = [red_line, yellow_line, blue_line_1, blue_line_2, green_line, violet_line, pink_line, magenta_line, grey_line, airport_express_orange_line, rapid_metro_gurgaon]

distance = [
    1154.48,  # Red Line
    1277.03,  # Yellow Line
    1111.20,  # Blue Line 3
    1028.75,  # Blue Line 4
    1165.00,  # Green Line
    1323.53,  # Violet Line
    1513.95,  # Pink Line
    1402.31,  # Magenta Line
    1245.00,  # Grey Line
    3557.14,  # Orange Line (Airport Express)
    961.82    # Rapid Metro (Gurgaon)
]

interchange_stations = [
    # Red Line Interchanges
    "kashmere gate", "inderlok", "netaji subhash place", "welcome",

    # Yellow Line Interchanges
    "kashmere gate", "rajiv chowk", "new delhi", "central secretariat", "hauz khas",
    "sikanderpur", "azadpur", "dilli haat - ina",

    # Blue Line 1 Interchanges
    "rajiv chowk", "mandi house", "kirti nagar", "dwarka sector - 21", "botanical garden",
    "yamuna bank", "mayur vihar - i", "karkarduma", "anand vihar isbt", "noida sector 52",

    # Blue Line 2 Interchanges
    "yamuna bank", "karkarduma", "anand vihar isbt",

    # Green Line Interchanges
    "kirti nagar", "inderlok", "netaji subhash place", "ashok park main",

    # Violet Line Interchanges
    "kashmere gate", "central secretariat", "mandi house", "lajpat nagar", "kalkaji mandir",

    # Pink Line Interchanges
    "majlis park", "azadpur", "netaji subhash place", "shakurpur", "rajouri garden",
    "mayur vihar - i", "karkarduma", "anand vihar isbt", "lajpat nagar", "dilli haat - ina",
    "sarai kale khan - hazrat nizamuddin",

    # Magenta Line Interchanges
    "botanical garden", "hauz khas", "janakpuri west", "kalkaji mandir",

    # Grey Line Interchange
    "dwarka",

    # Airport Express - Orange Line Interchanges
    "new delhi", "dwarka sector - 21", "yashobhoomi dwarka sector - 25",

    # Rapid Metro Interchange
    "sikanderpur"
]



# Create a graph
graph = nx.Graph()



# Loop through each metro line and its respective average distance
for i, line in enumerate(lines):  # Use enumerate to get index and stations list
    avg_distance = distance[i]  # Get corresponding average distance
    
    for j in range(len(line) - 1):  # Loop through stations in the line
        station1 = line[j]
        station2 = line[j + 1]

        graph.add_node(station1)  # Add station1 as a node
        graph.add_node(station2)  # Add station2 as a node
        graph.add_edge(station1, station2, weight=avg_distance)  # Connect stations

# Connect Interchange Stations
for station in interchange_stations:
    connected_lines = station  # Get all lines passing through this station
    for i in range(len(connected_lines) - 1):
        for j in range(i + 1, len(connected_lines)):
            line1 = connected_lines[i]
            line2 = connected_lines[j]
            graph.add_edge(line1, line2, weight=50)  # Small weight for interchanges



def show_graph(graph):
    plt.figure(figsize=(25, 25))
    pos = nx.spring_layout(graph, seed=42)  # Layout for visualization
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', edge_color='gray', font_size=8, node_size=20)
    plt.title("Delhi Metro Network")
    plt.show()


