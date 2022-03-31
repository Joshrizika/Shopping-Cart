PRAGMA foreign_keys=off;

DROP TABLE IF EXISTS users;
CREATE TABLE users (
  email         varchar(50) not null,
  fname          varchar(32) not null,
  lname          varchar(32) not null,
  password      varchar(50) not null,
  primary key (email),
  unique (password)
);

DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
  order_id            char(9) not null,
  customer_email      varchar(50) not null,
  date_ordered        date not null,
  time_ordered        time not null,
  total               decimal(10,2) not null,
  primary key (order_id),
  foreign key (customer_email) references users(email)
);

DROP TABLE IF EXISTS order_item;
CREATE TABLE order_item (
  order_item_id      char(9) not null,
  customer_email      varchar(50) not null,
  date_ordered        date not null,
  product_id          varchar(32) not null,
  order_id            char(9) not null,
  quantity            int(5) not null,
  primary key (order_item_id),
  foreign key (customer_email) references orders(customer_email),
  foreign key (date_ordered) references orders(date_ordered),
  foreign key (product_id) references product(id),
  foreign key (order_id) references orders(order_id)
);

DROP TABLE IF EXISTS product;
CREATE TABLE product (
  id           char(9) not null,
  name         varchar(50) not null,
  description  varchar(100) not null,
  price        decimal(10,2) not null,
  stock        int(5) not null,
  category     varchar(50) not null,
  primary key (id),
  foreign key (category) references category(name)
);

DROP TABLE IF EXISTS category;
CREATE TABLE category (
  name       varchar(50) not null,
  primary key (name)
);

PRAGMA foreign_keys=on;

INSERT INTO users VALUES ('testuser@gmail.com', 'Test', 'User', 'testpass');

INSERT INTO category VALUES ('Armor');
INSERT INTO product VALUES ('00001', 'Diamond Helmet', 'Helmets are a type of armor that covers the head of the player.', 45, 5, 'Armor');
INSERT INTO product VALUES ('00002', 'Diamond Chestplate', 'Chestplates are a type of armor that covers the upper body of the player.', 60, 5, 'Armor');
INSERT INTO product VALUES ('00003', 'Diamond Leggings', 'Leggings are a type of armor that covers the lower body of the player.', 50, 5, 'Armor');
INSERT INTO product VALUES ('00004', 'Diamond Boots', 'Boots are a type of armor that covers the feet of the player.', 40, 5, 'Armor');

INSERT INTO category VALUES ('Food');
INSERT INTO product VALUES ('00005', 'Bread', 'Bread is a food item that can be eaten by the player.  It restores 5 hunger.', 3, 50, 'Food');
INSERT INTO product VALUES ('00006', 'Cookie', 'Cookies are food items that can be obtained in large quantities, but do not restore hunger or saturation significantly.  They restore 2 hunger.', 5, 30, 'Food');
INSERT INTO product VALUES ('00007', 'Pumpkin Pie', 'Pumpkin Pie is a food item that can be eaten by the player.  It restores 8 hunger.', 8, 25, 'Food');
INSERT INTO product VALUES ('00008', 'Cake', 'Cake is a food and a block that can be eaten by the player. It has 7 slices and restores 2 hunger per slice.', 10, 15, 'Food');
INSERT INTO product VALUES ('00009', 'Golden Apple', 'The golden apple is a special food item that bestows beneficial effects when consumed.  It restores 4 hunger.', 15, 7, 'Food');

INSERT INTO category VALUES ('Enchanted Books');
INSERT INTO product VALUES ('00010', 'Mending', 'Mending is an enchantment that restores durability of an item using experience.', 75, 3, 'Enchanted Books');
INSERT INTO product VALUES ('00011', 'Unbreaking III', 'Unbreaking is an enchantment that gives a chance for an item to avoid durability reduction when it is used, effectively increasing the item''s durability.', 40, 5, 'Enchanted Books');
INSERT INTO product VALUES ('00012', 'Channeling', 'Channeling is a trident enchantment that produces lightning.', 35, 4, 'Enchanted Books');
INSERT INTO product VALUES ('00013', 'Curse of Binding', 'Curse of Binding is an enchantment that prevents removal of a cursed item from its armor slot.', 1, 50, 'Enchanted Books');
INSERT INTO product VALUES ('00014', 'Silk Touch', 'Silk Touch is a tool enchantment that causes certain blocks to drop themselves instead of their usual items when mined.', 30, 3, 'Enchanted Books');

INSERT INTO category VALUES ('Weapons');
INSERT INTO product VALUES ('00015', 'Netherite Sword', 'A sword is a melee weapon that is mainly used to damage entities and for cutting cobwebs or bamboo.', 50, 5, 'Weapons');
INSERT INTO product VALUES ('00016', 'Trident', 'A trident is a weapon used in both melee and ranged combat and is a rare drop from drowned.', 45, 4, 'Weapons');
INSERT INTO product VALUES ('00017', 'Bow', 'A bow is a ranged weapon that shoots arrows.', 15, 20, 'Weapons');
INSERT INTO product VALUES ('00018', 'Snowballs', 'Snowballs are throwable combat items.', 1, 100, 'Weapons');

INSERT INTO category VALUES ('Tools');
INSERT INTO product VALUES ('00019', 'Golden Pickaxe', 'A pickaxe is one of the most commonly used tools in the game, being required to mine all ores, rock, rock-based blocks and metal-based blocks.', 30, 15, 'Tools');
INSERT INTO product VALUES ('00020', 'Iron Axe', 'An axe is a tool mainly used to hasten the breaking of wood-based blocks, remove the surface layer of certain blocks, and as a melee weapon.', 25, 12, 'Tools');
INSERT INTO product VALUES ('00021', 'Netherite Hoe', 'A hoe is a tool used to till dirt and grass blocks into farmland, as well as to harvest certain plant-based blocks quickly.', 45, 5, 'Tools');
INSERT INTO product VALUES ('00022', 'Fishing Rod', 'A fishing rod is a tool used primarily for fishing.', 10, 20, 'Tools');

