import mysql.connector
from test_gatheritems import getData

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="rootpass",
  database="ammo"
)

mycursor = db.cursor()

# create ammo database below
# mycursor.execute("CREATE DATABASE ammo")

# create ammolisting table
# mycursor.execute("CREATE TABLE ammo_listings (listingID int PRIMARY KEY AUTO_INCREMENT, link VARCHAR(50), img VARCHAR(50), price DECIMAL(4,2), name VARCHAR(50), pper DECIMAL(2,2), caliber VARCHAR(20))")

#sample_ammo = [{'id': 0, 'link': 'https://palmettostatearmory.com/bps-ammunition-12ga-00-buckshot-2-3-4-1-2oz-10rd-box-bps12ga9pellet-00-2-75.html', 'img': 'https://palmettostatearmory.com/media/catalog/product/cache/152980d312fe5b5cdae0fdd9913a70b7/b/p/bps-ammunition-12ga-00-buckshot-2-3-4-1-2oz-10rd-box.jpg', 'name': 'BPS Ammunition 12ga 00 Buckshot 2 3/4" 1.2oz 10rd box - BPS12GA9PELLET-00-2.75', 'price': '$14.99', 'p_per': None}, {'id': 1, 'link': 'https://palmettostatearmory.com/browning-tss-tungsten-turkey-3-12-gauge-ammo-7-9-5-box-b193922030.html', 'img': 'https://palmettostatearmory.com/media/catalog/product/cache/152980d312fe5b5cdae0fdd9913a70b7/7/8/783901-Browning_TSS_Tungsten_Turkey_3_12_Gauge_Ammo_7_9_5_box_B193922030.jpg', 'name': 'Browning TSS Tungsten Turkey 3" 12 Gauge Ammo 5/box 10 cs - B193922030', 'price': '$39.99', 'p_per': '$8.00'}, {'id': 2, 'link': 'https://palmettostatearmory.com/hevi-shot-goose-3-12-gauge-ammo-4-10-box-45354.html', 'img': 'https://palmettostatearmory.com/media/catalog/product/cache/152980d312fe5b5cdae0fdd9913a70b7/7/8/784595-Hevi-Shot_Goose_3_12_Gauge_Ammo_4_10_box_45354.jpg', 'name': 'Hevi-Shot Goose 3" 12 Gauge Ammo 4, 10/box - 45354', 'price': '$45.48', 'p_per': '$4.55'}, {'id': 3, 'link': 'https://palmettostatearmory.com/hevi-shot-goose-3-5-12-gauge-ammo-b-10-box-43578.html', 'img': 'https://palmettostatearmory.com/media/catalog/product/cache/152980d312fe5b5cdae0fdd9913a70b7/7/8/784593-Hevi-Shot_Goose_3.5_12_Gauge_Ammo_B_10_box_43578.jpg', 'name': 'Hevi-Shot Goose 3.5" 12 Gauge Ammo B, 10/box - 43578', 'price': '$50.08', 'p_per': '$5.01'}, {'id': 4, 'link': 'https://palmettostatearmory.com/hevi-shot-goose-3-5-12-gauge-ammo-4-10-box-43574.html', 'img': 'https://palmettostatearmory.com/media/catalog/product/cache/152980d312fe5b5cdae0fdd9913a70b7/7/8/784592-Hevi-Shot_Goose_3.5_12_Gauge_Ammo_4_10_box_43574.jpg', 'name': 'Hevi-Shot Goose 3.5" 12 Gauge Ammo 4, 10/box - 43574', 'price': '$50.08', 'p_per': '$5.01'}, {'id': 5, 'link': 'https://palmettostatearmory.com/hevi-shot-classic-doubles-3-12-gauge-ammo-7-10-box-11137.html', 'img': 'https://palmettostatearmory.com/media/catalog/product/cache/152980d312fe5b5cdae0fdd9913a70b7/7/8/784546-Hevi-Shot_Classic_Doubles_3_12_Gauge_Ammo_7_10_box_11137.jpg', 'name': 'Hevi-Shot Classic Doubles 3" 12 Gauge Ammo 7, 10/box - 11137', 'price': '$48.28', 'p_per': '$4.83'}, {'id': 6, 'link': 'https://palmettostatearmory.com/hevi-shot-hevi-bismuth-waterfowl-2-75-12-gauge-ammo-2-25-box-14702.html', 'img': 'https://palmettostatearmory.com/media/catalog/product/cache/152980d312fe5b5cdae0fdd9913a70b7/7/8/784535-hevi-shot-ammo.jpg', 'name': 'Hevi-Shot Hevi-Bismuth Waterfowl 2.75" 12 Gauge Ammo 2, 25/box - 14702', 'price': '$39.99', 'p_per': '$1.60'}, {'id': 7, 'link': 'https://palmettostatearmory.com/fiocchi-shotgun-blank-12-gauge-ammo-25-box-12blank.html', 'img': 'https://palmettostatearmory.com/media/catalog/product/cache/152980d312fe5b5cdae0fdd9913a70b7/7/8/784304-Fiocchi_Shotgun_Blank_12_Gauge_Ammo_25_box_12BLANK.jpg', 'name': 'Fiocchi Shotgun Blank 12 Gauge Ammo, 25/box - 12BLANK', 'price': '$19.99', 'p_per': '$0.80'}, {'id': 8, 'link': 'https://palmettostatearmory.com/federal-heavyweight-tss-12-ga-3-5-2-5-oz-8-10-shot-5-shotshells-ptssx195f-810.html', 'img': 'https://palmettostatearmory.com/media/catalog/product/cache/152980d312fe5b5cdae0fdd9913a70b7/1/7/175724-PTSSX195F-810.jpg', 'name': 'Federal Heavyweight TSS 12 ga 3.5" 2.5 oz. #8,10 Shot, 5 Shotshells - PTSSX195F 810', 'price': '$69.99', 'p_per': '$14.00'}, {'id': 9, 'link': 'https://palmettostatearmory.com/hevi-shot-hevi-bismuth-3-5-10-gauge-ammo-2-25-box-15502.html', 'img': 'https://palmettostatearmory.com/media/catalog/product/cache/152980d312fe5b5cdae0fdd9913a70b7/7/9/793732-Hevi-Shot-Hevi-Bismuth_3.5_10_Gauge_Ammo_2_25_box-15502.jpg', 'name': 'Hevi-Shot Hevi-Bismuth 3.5" 10 Gauge Ammo 2, 25/box - 15502', 'price': '$59.98', 'p_per': '$2.40'}, {'id': 10, 'link': 'https://palmettostatearmory.com/hevi-shot-hevi-steel-3-5-10-gauge-ammo-bb-25-box-61088.html', 'img': 'https://palmettostatearmory.com/media/catalog/product/cache/152980d312fe5b5cdae0fdd9913a70b7/7/8/784619-Hevi-Shot_Hevi-Steel_3.5_10_Gauge_Ammo_BB_25_box_61088.jpg', 'name': 'Hevi-Shot Hevi-Steel 3.5" 10 Gauge Ammo BB, 25/box - 61088', 'price': '$35.88', 'p_per': '$1.44'}]

mycursor.execute("TRUNCATE TABLE ammo_listings")

sample_ammo = getData()

# modify size of columns
# mycursor.execute("ALTER TABLE ammo_listings MODIFY COLUMN link VARCHAR(200), MODIFY COLUMN img VARCHAR(200), MODIFY COLUMN name VARCHAR(100)")

# modify pper column to allow null
# mycursor.execute("ALTER TABLE ammo_listings MODIFY COLUMN pper DECIMAL(4,2) NULL")

# modify price column to permit like 0000.00 listings
# mycursor.execute("ALTER TABLE ammo_listings MODIFY COLUMN price DECIMAL(6,2) NULL")

# # remove '$' from price and p_per
for i, x in enumerate(sample_ammo):
  if(sample_ammo[i]["price"] is not None):
    sample_ammo[i]["price"] = sample_ammo[i]["price"][1:]
  if(sample_ammo[i]["p_per"] is not None):
    sample_ammo[i]["p_per"] = sample_ammo[i]["p_per"][1:]

# print(sample_ammo)

# add element into table
for x in sample_ammo:
  mycursor.execute("INSERT INTO ammo_listings (link, img, price, name, pper, caliber) VALUES (%s, %s, %s, %s, %s, %s)", (x["link"], x["img"], x["price"], x["name"], x["p_per"], "caliber"))
db.commit()