import media
import fresh_tomatoes

# Creates movie instances
sweet_november = media.Movie(
    "Sweet November",
    "Nelson Moss (Keanu Reeves) and Sara Deever (Charlize Theron) have nothing \
    in common except an hour spent in DMV hell. Intrigued by each other, but \
    not quite ready to commit, they settle on a rather unconventional \
    courtship: a one-month trial, after which they'll go their separate ways. \
    No expectations. No pressure. No strings attached. What neither of them \
    counts on is falling in love.",
    "https://upload.wikimedia.org/wikipedia/en/1/1b/SweetNovember2.jpg",
    "https://www.youtube.com/watch?v=A7hkvdyG8x4"
)

titanic = media.Movie(
    "Titanic",
    "James Cameron's 'Titanic' is an epic, action-packed romance set against \
    the ill-fated maiden voyage of the R.M.S. Titanic; the pride and joy of \
    the White Star Line and, at the time, the largest moving object ever \
    built. She was the most luxurious liner of her era -- the 'ship of \
    dreams' -- which ultimately carried over 1,500 people to their death in \
    the ice cold waters of the North Atlantic in the early hours of April 15, \
    1912.",
    "https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg",
    "https://www.youtube.com/watch?v=zCy5WQ9S4c0"
)

saw = media.Movie(
    "Saw",
    "Photographer Adam Stanheight (Leigh Whannell) and oncologist Lawrence \
    Gordon (Cary Elwes) regain consciousness while chained to pipes at either \
    end of a filthy bathroom. As the two men realize they've been trapped by \
    a sadistic serial killer nicknamed 'Jigsaw' and must complete his \
    perverse puzzle to live, flashbacks relate the fates of his previous \
    victims. Meanwhile, Dr. Gordon's wife (Monica Potter) and young daughter \
    (Makenzie Vega) are forced to watch his torture via closed-circuit video.",
    "https://upload.wikimedia.org/wikipedia/en/5/56/Saw_official_poster.jpg",
    "https://www.youtube.com/watch?v=OCZp5v8V-94"
)

black_swam = media.Movie(
    "Black Swan",
    "Nina (Natalie Portman) is a ballerina whose passion for the dance rules \
    every facet of her life. When the company's artistic director decides to \
    replace his prima ballerina for their opening production of 'Swan Lake', \
    Nina is his first choice. She has competition in newcomer Lily (Mila \
    Kunis) however. While Nina is perfect for the role of the White Swan, \
    Lily personifies the Black Swan. As rivalry between the two dancers \
    transforms into a twisted friendship, Nina's dark side begins to emerge.",
    "https://upload.wikimedia.org/wikipedia/en/6/68/Black_Swan_poster.jpg",
    "https://www.youtube.com/watch?v=5jaI1XOB-bs"
)

x_men_origins = media.Movie(
    "X-Men Origins: Wolverine",
    "Seeking solace from his dark past, Logan (Hugh Jackman), better known as \
    Wolverine, seems to have found love and contentment with Kayla Silverfox \
    (Lynn Collins). Logan's peaceful existence is shattered when Victor Creed \
    (Liev Schreiber), his vicious brother, brutally murders Kayla. Logan's \
    thirst for revenge propels him into the Weapon X program, where he \
    undergoes a painful procedure to bond his bones with adamantium, making \
    him virtually indestructible and more than a match for Victor.",
    "https://upload.wikimedia.org/wikipedia/en/e/ec/\
    X-Men_Origins_Wolverine.jpg",
    "https://www.youtube.com/watch?v=8TQ-gD4UCmI"
)

brokeback_montain = media.Movie(
    "Brokeback Montain",
    "In 1963, rodeo cowboy Jack Twist (Jake Gyllenhaal) and ranch hand Ennis \
    Del Mar (Heath Ledger) are hired by rancher Joe Aguirre (Randy Quaid) as \
    sheep herders in Wyoming. One night on Brokeback Mountain, Jack makes a \
    drunken pass at Ennis that is eventually reciprocated. Though Ennis \
    marries his longtime sweetheart, Alma (Michelle Williams), and Jack \
    marries a fellow rodeo rider (Anne Hathaway), the two men keep up their \
    tortured and sporadic affair over the course of 20 years.",
    "https://upload.wikimedia.org/wikipedia/en/a/a1/Brokeback_mountain.jpg",
    "https://www.youtube.com/watch?v=Tm4SlVWkdUU"
)

# Creates a list of the movie instances
movies = [
    sweet_november,
    titanic,
    saw,
    black_swam,
    x_men_origins,
    brokeback_montain
]

# Calls fresh_tomatoes function,
# Creates and renders the HTML file with movie selection
fresh_tomatoes.open_movies_page(movies=movies)
