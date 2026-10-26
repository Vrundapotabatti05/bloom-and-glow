export const UPI_ID = 'bloomglow@upi';
export const BANK_DETAILS = {
  "bank_name": "HDFC Bank",
  "account_name": "Bloom & Glow Pvt. Ltd.",
  "account_number": "50100234567890",
  "ifsc": "HDFC0001234",
  "branch": "MG Road, Bangalore",
  "account_type": "Current Account"
} as const;

export type Product = {
  name: string;
  price: number;
  original_price: number;
  discount: number;
  emoji: string;
  desc: string;
  rating?: number;
  reviews?: number;
  material?: string;
  weight?: string;
  burn_time?: string;
  occasion?: string;
  features?: string[];
  size?: string;
  color?: string;
  type?: string;
  chain_length?: string;
  [key: string]: any;
};

export const products: Record<string, Product[]> = {
  "Candles": [
    {
      "name": "Lavender Dream Candle",
      "price": 599,
      "original_price": 899,
      "discount": 33,
      "emoji": "🕯️",
      "desc": "Hand-poured soy candle with real lavender buds for a calming aromatherapy experience.",
      "rating": 4.8,
      "reviews": 324,
      "material": "100% Natural Soy Wax",
      "weight": "250g",
      "burn_time": "40 hours",
      "occasion": "Relaxation, Meditation",
      "features": [
        "Hand-poured",
        "Eco-friendly",
        "Cotton wick",
        "Non-toxic",
        "Reusable jar"
      ]
    },
    {
      "name": "Rose Petal Candle Set",
      "price": 899,
      "original_price": 1299,
      "discount": 31,
      "emoji": "🌹",
      "desc": "Set of 3 romantic rose-scented candles in elegant glass holders.",
      "rating": 4.7,
      "reviews": 256,
      "material": "Soy & Beeswax Blend",
      "weight": "3 x 150g",
      "burn_time": "30 hours each",
      "occasion": "Anniversary, Date Night",
      "features": [
        "Set of 3",
        "Glass holders included",
        "Romantic fragrance",
        "Long lasting",
        "Gift ready"
      ]
    },
    {
      "name": "Vanilla Bliss Candle",
      "price": 449,
      "original_price": 699,
      "discount": 36,
      "emoji": "✨",
      "desc": "Creamy vanilla bean scented candle that fills your room with warmth.",
      "rating": 4.9,
      "reviews": 512,
      "material": "Pure Soy Wax",
      "weight": "200g",
      "burn_time": "35 hours",
      "occasion": "Everyday, Gifting",
      "features": [
        "Bestseller",
        "Premium vanilla extract",
        "Smokeless",
        "Even burn",
        "Ceramic jar"
      ]
    },
    {
      "name": "Berry Bonanza Candle",
      "price": 699,
      "original_price": 999,
      "discount": 30,
      "emoji": "🫐",
      "desc": "Mixed berry fragrance with sparkling glitter finish for a festive vibe.",
      "rating": 4.6,
      "reviews": 189,
      "material": "Soy Wax with Glitter",
      "weight": "280g",
      "burn_time": "42 hours",
      "occasion": "Parties, Celebrations",
      "features": [
        "Glitter finish",
        "Berry blend scent",
        "Handcrafted",
        "Lead-free wick",
        "Luxury packaging"
      ]
    },
    {
      "name": "Cherry Blossom Candle",
      "price": 799,
      "original_price": 1199,
      "discount": 33,
      "emoji": "🌸",
      "desc": "Delicate Japanese cherry blossom scent in a beautiful pink jar.",
      "rating": 4.8,
      "reviews": 298,
      "material": "Coconut & Soy Blend",
      "weight": "300g",
      "burn_time": "45 hours",
      "occasion": "Self-care, Gifting",
      "features": [
        "Japanese inspired",
        "Premium fragrance",
        "Pink ceramic jar",
        "45hr burn",
        "Vegan friendly"
      ]
    },
    {
      "name": "Cotton Candy Candle",
      "price": 549,
      "original_price": 799,
      "discount": 31,
      "emoji": "🍭",
      "desc": "Sweet cotton candy fragrance that brings back childhood memories.",
      "rating": 4.5,
      "reviews": 203,
      "material": "Soy Wax",
      "weight": "220g",
      "burn_time": "38 hours",
      "occasion": "Kids room, Fun gifting",
      "features": [
        "Sweet scent",
        "Fun design",
        "Safe for kids",
        "Cotton wick",
        "Glass container"
      ]
    }
  ],
  "Corset Flowers": [
    {
      "name": "Pink Satin Corset Bouquet",
      "price": 1499,
      "original_price": 2199,
      "discount": 32,
      "emoji": "💐",
      "desc": "Silk flowers elegantly arranged in a luxury satin corset wrap.",
      "rating": 4.9,
      "reviews": 445,
      "material": "Premium Silk Flowers",
      "size": "Medium (12 inches)",
      "color": "Baby Pink",
      "occasion": "Valentine's, Anniversary",
      "features": [
        "Lasts forever",
        "Satin ribbon wrap",
        "12 silk flowers",
        "Gift box included",
        "Customizable"
      ]
    },
    {
      "name": "Purple Velvet Corset",
      "price": 1799,
      "original_price": 2599,
      "discount": 31,
      "emoji": "🌺",
      "desc": "Luxury velvet corset arrangement with deep purple artificial flowers.",
      "rating": 4.8,
      "reviews": 334,
      "material": "Velvet & Silk",
      "size": "Large (15 inches)",
      "color": "Royal Purple",
      "occasion": "Birthday, Mother's Day",
      "features": [
        "Velvet texture",
        "Premium flowers",
        "Elegant packaging",
        "Photo-ready",
        "Preserved blooms"
      ]
    },
    {
      "name": "Baby Pink Dream",
      "price": 1299,
      "original_price": 1899,
      "discount": 32,
      "emoji": "🎀",
      "desc": "Delicate pink roses wrapped in a corset-style arrangement with bow.",
      "rating": 4.7,
      "reviews": 287,
      "material": "Silk & Satin",
      "size": "Small (10 inches)",
      "color": "Baby Pink",
      "occasion": "Propose, Valentine's",
      "features": [
        "Bow detail",
        "Silk roses",
        "Compact size",
        "Gift tag included",
        "Eco-friendly"
      ]
    },
    {
      "name": "Lavender Fields Corset",
      "price": 1599,
      "original_price": 2299,
      "discount": 30,
      "emoji": "💜",
      "desc": "Lavender arrangement with corset detail and dried flower accents.",
      "rating": 4.6,
      "reviews": 198,
      "material": "Dried & Artificial Flowers",
      "size": "Medium (13 inches)",
      "color": "Lavender",
      "occasion": "Wedding, Housewarming",
      "features": [
        "Dried flowers",
        "Long lasting",
        "Corset design",
        "Natural scent",
        "Handmade"
      ]
    },
    {
      "name": "Sunset Blush Corset",
      "price": 1699,
      "original_price": 2499,
      "discount": 32,
      "emoji": "🌺",
      "desc": "Orange and pink gradient corset bouquet for a warm, vibrant look.",
      "rating": 4.8,
      "reviews": 256,
      "material": "Premium Silk",
      "size": "Large (14 inches)",
      "color": "Orange-Pink Gradient",
      "occasion": "Birthday, Congrats",
      "features": [
        "Gradient design",
        "Vibrant colors",
        "Premium wrap",
        "Photo-perfect",
        "Luxury feel"
      ]
    },
    {
      "name": "Royal Purple Corset",
      "price": 1999,
      "original_price": 2899,
      "discount": 31,
      "emoji": "👑",
      "desc": "Premium purple flowers in a regal corset arrangement with golden accents.",
      "rating": 4.9,
      "reviews": 412,
      "material": "Silk & Gold Foil",
      "size": "X-Large (16 inches)",
      "color": "Royal Purple",
      "occasion": "VIP Gifting, Weddings",
      "features": [
        "Gold accents",
        "Premium flowers",
        "Royal design",
        "Velvet box",
        "Personalized tag"
      ]
    }
  ],
  "Bouquets": [
    {
      "name": "Romantic Red Roses",
      "price": 999,
      "original_price": 1499,
      "discount": 33,
      "emoji": "🌹",
      "desc": "12 long-stem red roses with baby's breath, wrapped in luxury paper.",
      "rating": 4.9,
      "reviews": 856,
      "material": "Fresh Red Roses",
      "size": "Standard Bouquet",
      "color": "Red",
      "occasion": "Valentine's, Proposal",
      "features": [
        "12 long-stem roses",
        "Baby's breath included",
        "Luxury wrapping",
        "Free card",
        "Same day delivery"
      ]
    },
    {
      "name": "Pastel Paradise Bouquet",
      "price": 1299,
      "original_price": 1899,
      "discount": 32,
      "emoji": "🌸",
      "desc": "Mixed pastel flowers including pink, peach, and lilac blooms.",
      "rating": 4.7,
      "reviews": 334,
      "material": "Mixed Fresh Flowers",
      "size": "Large Bouquet",
      "color": "Pastel Mix",
      "occasion": "Birthday, Thank You",
      "features": [
        "20+ stems",
        "Mixed pastels",
        "Seasonal flowers",
        "Eco wrapping",
        "Care guide"
      ]
    },
    {
      "name": "Wildflower Bliss",
      "price": 899,
      "original_price": 1299,
      "discount": 31,
      "emoji": "🌻",
      "desc": "Rustic wildflower bouquet with a hand-tied burlap wrap.",
      "rating": 4.6,
      "reviews": 223,
      "material": "Fresh Wildflowers",
      "size": "Medium Bouquet",
      "color": "Multi-color",
      "occasion": "Housewarming, Get Well",
      "features": [
        "Rustic design",
        "Burlap wrap",
        "Wild assortment",
        "Fragrant",
        "Natural look"
      ]
    },
    {
      "name": "Peony Dream Bouquet",
      "price": 1599,
      "original_price": 2299,
      "discount": 30,
      "emoji": "🌷",
      "desc": "Fresh pink peonies in luxury gold-foil wrapping.",
      "rating": 4.9,
      "reviews": 567,
      "material": "Fresh Peonies",
      "size": "Premium Bouquet",
      "color": "Blush Pink",
      "occasion": "Wedding, Anniversary",
      "features": [
        "Premium peonies",
        "Gold foil wrap",
        "Fragrant blooms",
        "Gift bag included",
        "Nationwide delivery"
      ]
    },
    {
      "name": "Sunflower Sunshine",
      "price": 799,
      "original_price": 1199,
      "discount": 33,
      "emoji": "🌻",
      "desc": "Bright sunflower arrangement to bring joy and warmth.",
      "rating": 4.8,
      "reviews": 445,
      "material": "Fresh Sunflowers",
      "size": "Standard Bouquet",
      "color": "Yellow",
      "occasion": "Birthday, Get Well Soon",
      "features": [
        "Cheerful blooms",
        "Long stems",
        "Bright yellow",
        "Eco-friendly wrap",
        "Photo-ready"
      ]
    },
    {
      "name": "Mixed Tulip Bouquet",
      "price": 1199,
      "original_price": 1799,
      "discount": 33,
      "emoji": "🌷",
      "desc": "Colorful tulips for any occasion, arranged in a cone wrap.",
      "rating": 4.7,
      "reviews": 312,
      "material": "Fresh Tulips",
      "size": "Standard Bouquet",
      "color": "Multi-color",
      "occasion": "Spring, Any Celebration",
      "features": [
        "15 fresh tulips",
        "Cone wrap design",
        "Vibrant colors",
        "Fragile-safe packing",
        "Same day dispatch"
      ]
    }
  ],
  "Jewelries": [
    {
      "name": "Rose Gold Necklace Set",
      "price": 1999,
      "original_price": 2999,
      "discount": 33,
      "emoji": "💍",
      "desc": "Elegant rose gold plated necklace with matching drop earrings.",
      "rating": 4.8,
      "reviews": 389,
      "material": "Rose Gold Plated Brass",
      "type": "Necklace & Earrings Set",
      "chain_length": "18 inches",
      "occasion": "Party, Anniversary",
      "features": [
        "Tarnish free",
        "Nickel free",
        "Adjustable chain",
        "Gift box included",
        "Hypoallergenic"
      ]
    },
    {
      "name": "Pearl Drop Earrings",
      "price": 899,
      "original_price": 1299,
      "discount": 31,
      "emoji": "💎",
      "desc": "Classic freshwater pearl earrings with gold plating.",
      "rating": 4.9,
      "reviews": 567,
      "material": "Freshwater Pearl & Gold",
      "type": "Drop Earrings",
      "size": "2 cm drop",
      "occasion": "Office, Formal Events",
      "features": [
        "Genuine pearl",
        "Gold plated",
        "Lightweight",
        "Elegant design",
        "Satin pouch"
      ]
    },
    {
      "name": "Heart Pendant Chain",
      "price": 1299,
      "original_price": 1899,
      "discount": 32,
      "emoji": "❤️",
      "desc": "Delicate heart pendant on a rose gold chain, perfect for gifting.",
      "rating": 4.7,
      "reviews": 423,
      "material": "Rose Gold Plated Silver",
      "type": "Pendant Necklace",
      "chain_length": "16-18 inches",
      "occasion": "Valentine's, Birthday",
      "features": [
        "Heart design",
        "Adjustable chain",
        "Sparkling stone",
        "Gift ready",
        "Anti-tarnish"
      ]
    },
    {
      "name": "Crystal Bracelet Set",
      "price": 1599,
      "original_price": 2299,
      "discount": 30,
      "emoji": "✨",
      "desc": "Set of 3 sparkling crystal bead bracelets in rose gold.",
      "rating": 4.6,
      "reviews": 278,
      "material": "Crystal & Rose Gold",
      "type": "Bracelet Set (3 pcs)",
      "size": "Adjustable",
      "occasion": "Party, Casual Wear",
      "features": [
        "Set of 3",
        "Crystal beads",
        "Stretchy band",
        "Stackable",
        "Gift pouch"
      ]
    },
    {
      "name": "Butterfly Ring",
      "price": 699,
      "original_price": 999,
      "discount": 30,
      "emoji": "🦋",
      "desc": "Adjustable butterfly ring in rose gold with crystal wings.",
      "rating": 4.8,
      "reviews": 445,
      "material": "Rose Gold & Crystal",
      "type": "Adjustable Ring",
      "size": "Free Size",
      "occasion": "Daily Wear, Gift",
      "features": [
        "Butterfly design",
        "Crystal wings",
        "Adjustable",
        "Comfortable fit",
        "Gift box"
      ]
    },
    {
      "name": "Diamond Stud Earrings",
      "price": 2499,
      "original_price": 3499,
      "discount": 29,
      "emoji": "💍",
      "desc": "Premium cubic zirconia stud earrings in white gold plating.",
      "rating": 4.9,
      "reviews": 678,
      "material": "CZ & White Gold",
      "type": "Stud Earrings",
      "size": "6mm stones",
      "occasion": "Wedding, Formal",
      "features": [
        "Sparkling CZ",
        "White gold",
        "Secure clasp",
        "Premium box",
        "Lifetime warranty"
      ]
    }
  ],
  "Beauty Products": [
    {
      "name": "Rose Quartz Face Roller",
      "price": 799,
      "original_price": 1199,
      "discount": 33,
      "emoji": "💫",
      "desc": "Natural rose quartz facial roller for skin massage and relaxation.",
      "rating": 4.8,
      "reviews": 456,
      "material": "100% Natural Rose Quartz",
      "type": "Face Roller",
      "size": "Dual-ended",
      "occasion": "Skincare, Self-care",
      "features": [
        "Dual-ended",
        "Cooling effect",
        "Reduces puffiness",
        "Silk pouch included",
        "Gift worthy"
      ]
    },
    {
      "name": "Pink Clay Face Mask",
      "price": 499,
      "original_price": 749,
      "discount": 33,
      "emoji": "🧖",
      "desc": "Gentle pink clay face mask set with 5 single-use packets.",
      "rating": 4.7,
      "reviews": 334,
      "material": "Pink Clay & Botanicals",
      "type": "Face Mask Set",
      "size": "5 x 15ml packets",
      "occasion": "Spa Day, Self-care",
      "features": [
        "5 packets",
        "Gentle formula",
        "Brightening",
        "Pore minimizing",
        "All skin types"
      ]
    },
    {
      "name": "Floral Lip Gloss Set",
      "price": 699,
      "original_price": 999,
      "discount": 30,
      "emoji": "💋",
      "desc": "Set of 4 floral scented lip glosses in pink shades.",
      "rating": 4.6,
      "reviews": 267,
      "material": "Natural Oils & Pigments",
      "type": "Lip Gloss Set",
      "size": "4 x 5ml",
      "occasion": "Daily Wear, Party",
      "features": [
        "4 shades",
        "Floral scented",
        "Moisturizing",
        "Non-sticky",
        "Cruelty free"
      ]
    },
    {
      "name": "Lavender Body Butter",
      "price": 599,
      "original_price": 899,
      "discount": 33,
      "emoji": "🧴",
      "desc": "Ultra-moisturizing lavender body butter for silky smooth skin.",
      "rating": 4.9,
      "reviews": 589,
      "material": "Shea Butter & Lavender Oil",
      "type": "Body Butter",
      "size": "250ml",
      "occasion": "Daily Skincare",
      "features": [
        "Deep moisturizing",
        "Natural lavender",
        "24hr hydration",
        "Paraben free",
        "Glass jar"
      ]
    },
    {
      "name": "Rose Water Toner",
      "price": 449,
      "original_price": 649,
      "discount": 31,
      "emoji": "🌹",
      "desc": "Pure rose water facial toner for refreshed, glowing skin.",
      "rating": 4.7,
      "reviews": 398,
      "material": "100% Pure Rose Water",
      "type": "Face Toner",
      "size": "200ml",
      "occasion": "Daily Skincare",
      "features": [
        "100% pure",
        "pH balanced",
        "Refreshing",
        "All skin types",
        "Spray bottle"
      ]
    },
    {
      "name": "Himalayan Bath Salts",
      "price": 399,
      "original_price": 599,
      "discount": 33,
      "emoji": "🛁",
      "desc": "Pink Himalayan bath salts with rose and jasmine essential oils.",
      "rating": 4.8,
      "reviews": 312,
      "material": "Himalayan Salt & Essential Oils",
      "type": "Bath Salt",
      "size": "500g",
      "occasion": "Bath Time, Relaxation",
      "features": [
        "500g jar",
        "Rose & jasmine",
        "Detoxifying",
        "Muscle relaxation",
        "Mason jar"
      ]
    }
  ],
  "Soft Toys": [
    {
      "name": "Giant Pink Teddy Bear",
      "price": 1999,
      "original_price": 2999,
      "discount": 33,
      "emoji": "🧸",
      "desc": "3ft tall ultra-soft teddy bear in baby pink with satin bow.",
      "rating": 4.9,
      "reviews": 789,
      "material": "Premium Plush Fabric",
      "size": "3 feet (90 cm)",
      "color": "Baby Pink",
      "occasion": "Birthday, Valentine's",
      "features": [
        "3ft tall",
        "Ultra soft",
        "Satin bow",
        "Surface washable",
        "Gift wrapped"
      ]
    },
    {
      "name": "Unicorn Plush Set",
      "price": 1299,
      "original_price": 1899,
      "discount": 32,
      "emoji": "🦄",
      "desc": "Set of 3 colorful unicorn plushies in pastel shades.",
      "rating": 4.8,
      "reviews": 456,
      "material": "Soft Plush & Polyester",
      "size": "3 x 20 cm",
      "color": "Pastel Rainbow",
      "occasion": "Kids, Collectors",
      "features": [
        "Set of 3",
        "Pastel colors",
        "Soft filling",
        "Machine washable",
        "Collectible"
      ]
    },
    {
      "name": "Bunny with Heart",
      "price": 799,
      "original_price": 1199,
      "discount": 33,
      "emoji": "🐰",
      "desc": "Soft bunny holding a red heart pillow, perfect for gifting.",
      "rating": 4.7,
      "reviews": 334,
      "material": "Plush & Velvet",
      "size": "35 cm",
      "color": "White & Pink",
      "occasion": "Valentine's, Love",
      "features": [
        "Heart pillow",
        "Velvet texture",
        "Super soft",
        "Safe for all ages",
        "Gift tag"
      ]
    },
    {
      "name": "Panda Couple Set",
      "price": 1499,
      "original_price": 2199,
      "discount": 32,
      "emoji": "🐼",
      "desc": "Matching panda plush couple that holds hands when placed together.",
      "rating": 4.9,
      "reviews": 567,
      "material": "Premium Plush",
      "size": "2 x 30 cm",
      "color": "Black & White",
      "occasion": "Couples, Anniversary",
      "features": [
        "Magnetic hands",
        "Couple set",
        "Super soft",
        "Premium quality",
        "Gift box"
      ]
    },
    {
      "name": "Dinosaur Plush Collection",
      "price": 999,
      "original_price": 1499,
      "discount": 33,
      "emoji": "🦕",
      "desc": "Set of 2 adorable dinosaur plushies in pastel green and pink.",
      "rating": 4.6,
      "reviews": 223,
      "material": "Soft Plush",
      "size": "2 x 25 cm",
      "color": "Pastel Green & Pink",
      "occasion": "Kids, Decor",
      "features": [
        "Set of 2",
        "Cute design",
        "Soft filling",
        "Non-toxic",
        "Kid safe"
      ]
    },
    {
      "name": "Rainbow Unicorn",
      "price": 1199,
      "original_price": 1799,
      "discount": 33,
      "emoji": "🌈",
      "desc": "Magical rainbow colored unicorn with a golden horn and wings.",
      "rating": 4.8,
      "reviews": 389,
      "material": "Plush & Satin",
      "size": "40 cm",
      "color": "Rainbow",
      "occasion": "Birthday, Fantasy",
      "features": [
        "Rainbow body",
        "Golden horn",
        "Winged design",
        "Light up option",
        "Premium quality"
      ]
    }
  ]
};
