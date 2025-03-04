import networkx as nx
import matplotlib.pyplot as plt


red = [
    "shaheed sthal (new bus adda)", "hindon river", "arthala", "mohan nagar", "shyam park",
    "major mohit sharma rajendra nagar", "raj bagh", "shaheed nagar", "dilshad garden", "jhil mil",
    "mansarovar park", "shahdara", "welcome", "seelampur", "shastri park", "kashmere gate",
    "tis hazari", "pul bangash", "pratap nagar", "shastri nagar", "inderlok",
    "kanhaiya nagar", "keshav puram", "netaji subhash place", "kohat enclave", "pitam pura",
    "rohini east", "rohini west", "rithala", "rajendra nagar", "modinagar", "meerut south"
]

yellow = [
    "samaypur badli", "rohini sector 18-19", "haiderpur badli mor", "jahangirpuri",
    "adarsh nagar", "azadpur", "model town", "guru tegh bahadur nagar", "vishwavidyalaya",
    "vidhan sabha", "civil lines", "kashmere gate", "chandni chowk", "chawri bazar",
    "new delhi", "rajiv chowk", "patel chowk", "central secretariat", "udyog bhawan",
    "lok kalyan marg", "jor bagh", "dilli haat ina", "aiims", "green park", "hauz khas",
    "malviya nagar", "saket", "qutab minar", "chhattarpur", "sultanpur", "ghitorni",
    "arjan garh", "guru dronacharya", "sikandarpur", "mg road", "iffco chowk", "huda city centre",
    "sector 23 dwarka", "dharampura", "bijwasan"
]

blue = [
    "dwarka sector 21", "dwarka sector 8", "dwarka sector 9", "dwarka sector 10",
    "dwarka sector 11", "dwarka sector 12", "dwarka sector 13", "dwarka sector 14",
    "dwarka", "dwarka mor", "nawada", "uttam nagar west", "uttam nagar east",
    "janak puri west", "janak puri east", "tilak nagar", "subhash nagar", "tagore garden",
    "rajouri garden", "ramesh nagar", "moti nagar", "kirti nagar", "shadipur",
    "patel nagar", "rajendra place", "karol bagh", "jhandewalan", "rk ashram marg",
    "rajiv chowk", "barakhamba", "mandi house", "supreme court (pragati maidan)",
    "indraprastha", "yamuna bank", "akshardham", "mayur vihar phase-1", "mayur vihar extension",
    "new ashok nagar", "noida sector 15", "noida sector 16", "noida sector 18",
    "botanical garden", "golf course", "noida city center", "noida sector 34",
    "noida sector 52", "noida sector 61", "noida sector 59", "noida sector 62",
    "noida electronic city", "noida sector 50", "noida sector 76", "noida sector 101",
    "noida sector 81", "noida sector 83", "noida sector 137", "noida sector 142",
    "noida sector 143", "noida sector 144", "noida sector 145", "noida sector 146",
    "noida sector 147", "noida sector 148", "knowledge park II", "pari chowk", "alpha 1",
    "alpha 2", "delta 1", "GNIDA office", "depot"
]

green = [
    "inderlok", "ashok park main", "punjabi bagh", "shivaji park", "madipur",
    "paschim vihar (east)", "paschim vihar (west)", "peera garhi", "udyog nagar",
    "maharaja surajmal stadium", "nangloi", "nangloi railway station", "rajdhani park",
    "mundka", "mundka industrial area", "ghevra metro station", "tikri kalan", "tikri border",
    "pandit shree ram sharma", "bahadurgarh city", "brigadier hoshiar singh", "sector 10 bahadurgarh"
]

violet = [
    "kashmere gate", "lal quila", "jama masjid", "delhi gate", "ito", "mandi house",
    "janpath", "central secretariat", "khan market", "jawaharlal nehru stadium",
    "jangpura", "lajpat nagar", "moolchand", "kailash colony", "nehru place",
    "kalkaji mandir", "govind puri", "okhla", "jasola", "sarita vihar", "mohan estate",
    "tughlakabad", "badarpur border", "sarai", "n.h.p.c. chowk", "mewala maharajpur",
    "sector 28 faridabad", "badkal mor", "old faridabad", "neelam chowk ajronda",
    "bata chowk", "escorts mujesar", "sant surdas - sihi", "raja nahar singh", "ballabhgarh", "ncb colony"
]

magenta = [
    "janak puri west", "hauz khas", "kalkaji mandir", "botanical garden", "saket g block", "lado sarai"
]

pink = [
    "majlis park", "azadpur", "shalimar bagh", "netaji subhash place", "shakurpur",
    "punjabi bagh west", "esi basai darapur", "rajouri garden", "maya puri",
    "naraina vihar", "delhi cantt", "durgabai deshmukh south campus",
    "sir vishweshwaraiah moti bagh", "bhikaji cama place", "sarojini nagar",
    "dilli haat ina", "south extension", "lajpat nagar", "vinobapuri", "ashram",
    "sarai kale khan hazrat nizamuddin", "maujpur", "majlis park"
]

aqua = [
    "dwarka sector 21", "noida sector 146", "noida sector 147", "noida sector 148"
]

lines = [red, yellow, blue, green, violet, magenta, pink, aqua]


# Create a graph
graph = nx.Graph()

# Add edges to the graph (connecting stations in each metro line)
for line in lines:
    for i in range(len(line) - 1):
        graph.add_edge(line[i], line[i + 1])

# Identify interchange stations
interchange_stations = {}
for line in lines:
    for station in line:
        if station in interchange_stations:
            interchange_stations[station].append(line)
        else:
            interchange_stations[station] = [line]

# Draw the graph
def show_graph(graph):
    plt.figure(figsize=(25, 25))
    pos = nx.spring_layout(graph, seed=42)  # Layout for visualization
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', edge_color='gray', font_size=8, node_size=20)
    plt.title("Delhi Metro Network")
    plt.show()


show_graph(graph)