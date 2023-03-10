from tkinter import *
from tkinter import ttk

def copy_final():
	root.clipboard_clear()
	multiple_sample = sample_entry.get()
	if category_type.get() == 'Cheats':
		pass
	else:
		for i in range(int(quantity_entry.get())-1):
			multiple_sample = multiple_sample + '|'+ sample_entry.get()
	root.clipboard_append(multiple_sample)

def category_select_match():
	cat_type = str(category_type.get())
	match cat_type:
		case 'Normal Creatures':
			selectionCombo['values'] = normal_creature_drop
			selectionCombo.set('')
		case 'Angry Creatures':
			selectionCombo['values'] = angry_creature_drop
			selectionCombo.set('')
		case 'Passive Creatures':
			selectionCombo['values'] = passive_creature_drop
			selectionCombo.set('')
		case 'Weapon Upgrade Materials':
			selectionCombo['values'] = weapon_upgrades_drop
			selectionCombo.set('')
		case 'Armor Upgrade Matierials':
			selectionCombo['values'] = armor_upgrades_drop
			selectionCombo.set('')
		case 'Smoothies':
			selectionCombo['values'] = smoothies_drop
			selectionCombo.set('')
		case 'Food':
			selectionCombo['values'] = food_drop
			selectionCombo.set('')
		case 'Crafting':
			selectionCombo['values'] = crafting_drop
			selectionCombo.set('')
		case 'Trinkets':
			selectionCombo['values'] = trinkets_drop
			selectionCombo.set('')
		case 'Cheats':
			selectionCombo['values'] = cheats_drop
			selectionCombo.set('')
		case 'Loadouts':
			selectionCombo['values'] = loudouts_drop
			selectionCombo.set('')
		case 'Arrows':
			selectionCombo['values'] = arrows_drop
			selectionCombo.set('')

def callback(eventObject):
	for b, c in creatureDict.items():
		if b==selection_type.get():
			sample.set(c)
			break

category_drop = ["Normal Creatures","Angry Creatures","Passive Creatures","Weapon Upgrade Materials","Armor Upgrade Matierials","Smoothies"
	,"Food","Crafting","Arrows","Trinkets","Loadouts","Cheats"]
normal_creature_drop = ['Bee', 'Black Worker Ant', 'Firefly', 'Ladybug', 'Moth', 'Red Worker Ant', 'Sickly Rolly Polly']
angry_creature_drop = ['ARC.R', 'Antlion', 'Assistant Manager', 'Black Ant Soldier', 'Black Ox Beetle', 'Black Widow', 'Black Widowling'
	, 'Bombardier Beetle', 'Director Schmector', 'Diving Bell Spider', 'Dust Mite', 'Fire Soldier Ant', 'Fire Worker Ant'
	, 'Green Shield Bug', 'Hedge Broodmother', 'Infected Gnat', 'Infected Ladybug', 'Infected Larva', 'Infected Weavil'
	, 'Infected Wolf Spider', 'Ladybird', 'Ladybird Larva', 'Larva', 'Lawn Mite', 'Mant', 'Mantis', 'Mosquito', 'Orb Weaver'
	, 'Orb Weaver Jr.', 'RUZ.T', 'Red Soldier Ant', 'Spiderling', 'Spiny Water Flea', 'Stinkbug', 'TAYZ.T', 'Termite King', 'Termite Soldier'
	, 'Termite Worker', 'Tick', 'Tiger Mosquito', 'Water Flea', 'Wolf Spider']
passive_creature_drop = ['Aphid', 'Gnat', 'Grub', 'Meaty Gnat', 'Scarab', 'Tadpole', 'Water Boatman', 'Weevil']
weapon_upgrades_drop = ["Mighty Jewel","Mint Jewel","Salt Jewel","Sour Jewel","Spicy Jewel","Mighty Glob","Mint Glob","Salt Glob","Sour Glob","Spicy Glob","Brittle Whetstone"]
armor_upgrades_drop = ["Supreme Plating","Sturdy Plating","Brittle Plating"]
smoothies_drop = ["Boost Juice","Fluid Flippers","Fuzz on the Rocks","Gastro Goo","Green Machine","Hedge Lord","Human Food","Liquid Gills"
	,"Liquid Rage","Questionable Slop", "Worker's Comp"]
food_drop = ["Black Ox Burger","Funguspacho","Gnatchos","Larvagna","Mac N Bees","Miteloaf","Omelant","Quesadillantlion"
	,"Spaghetflea","Spider Slider","Tadpoloca Pudding","Termite Delight","Broodmother BLT","Orchid Mantis Kebab"]
crafting_drop = ["Berry Chunk","Berry Leather","Bomb, Sticky","EverChar Coal Chunk","Lint Rope","Pebblet","Pond Moss","Pupa Hide","Pupa Leather","Spider Silk","Toenail"]
trinkets_drop = ['Biomedical Badge', 'Broodmother Trinket', 'Compliance Badge', 'Defense Badge', 'Entomologist Badge', 'Everlasting Hogstopper'
	, 'Fluffy Dandelion Tuft', 'Fungal Charm', 'Hot Cha Charm', 'Insulating Larva Spike', 'Intern Badge', 'Left Elf Charm'
	, 'Mantis Trinket', 'Power Droplet', 'Right Elf Charm', 'Rotten Berry Charm', "Serah's Charm", 'Shiny Salt Crystal'
	, 'Suspicious Ice Cap', "Thor's Pendant", 'Toxicology Badge', 'Wonderous Wormhole']
arrows_drop =["Bomb Arrow","Sour Arrow","Super Venom Arrow","Splinter Arrow"]
cheats_drop = ["Build All Buildings","Repair All Items","Full Restore","God Mode","Infinite Damage"]
loudouts_drop = ["Boost/Fuzz/Green/Rage Smoothies"]

creatureDict = {'Bee':"summon /Game/Blueprints/Creatures/Bee/Base/BP_Bee.uasset.BP_Bee_C"
	,'Black Worker Ant':"summon /Game/Blueprints/Creatures/Ant/Black/Worker/BP_Ant_Black.uasset.BP_Ant_Black_C"
	,'Firefly':"summon /Game/Blueprints/Creatures/Firefly/Base/BP_Firefly.uasset.BP_Firefly_C"
	,'Ladybug':"summon /Game/Blueprints/Creatures/Ladybug/Base/BP_Ladybug.uasset.BP_Ladybug_C"
	,'Moth':"summon /Game/Blueprints/Creatures/Moth/Base/BP_Moth.uasset.BP_Moth_C"
	,'Red Worker Ant':"summon /Game/Blueprints/Creatures/Ant/Red/Worker/BP_Ant.uasset.BP_Ant_C"
	,'Sickly Rolly Polly':"summon /Game/Blueprints/Creatures/RolyPoly/Base/BP_RolyPoly_Sickly.uasset.BP_RolyPoly_Sickly_C"
	,'ARC.R':"summon /Game/Blueprints/Creatures/TazT/ElectricRanged/BP_ArcR.uasset.BP_ArcR_C"
	,'Antlion':"summon /Game/Blueprints/Creatures/Antlion/Base/BP_Antlion_Roamer.uasset.BP_Antlion_Roamer_C"
	,'Assistant Manager':"summon /Game/Blueprints/Creatures/TazT/ElectricRanged/Miniboss/BP_ArcR_MKII.uasset.BP_ArcR_MKII_C"
	,'Black Ant Soldier':"summon /Game/Blueprints/Creatures/Ant/Black/Soldier/BP_Ant_Soldier_Black.uasset.BP_Ant_Soldier_Black_C"
	,'Black Ox Beetle':"summon /Game/Blueprints/Creatures/BlackOxBeetle/Base/BP_BlackOxBeetle.uasset.BP_BlackOxBeetle_C"
	,'Black Widow':"summon /Game/Blueprints/Creatures/Spider/BlackWidow/BP_Spider_BlackWidow.uasset.BP_Spider_BlackWidow_C"
	,'Black Widowling':"summon /Game/Blueprints/Creatures/Spider/Spiderling/BP_Spiderling_BlackWidow.uasset.BP_Spiderling_BlackWidow_C"
	,'Bombardier Beetle':"summon /Game/Blueprints/Creatures/BombardierBeetle/Base/BP_BombardierBeetle.uasset.BP_BombardierBeetle_C"
	,'Director Schmector':"summon /Game/Blueprints/Creatures/TazT/Boss/BP_Ominent_Robot.uasset.BP_Ominent_Robot_C"
	,'Diving Bell Spider':"summon /Game/Blueprints/Creatures/DivingBellSpider/Base/BP_DivingBellSpider.uasset.BP_DivingBellSpider_C"
	,'Dust Mite':"summon /Game/Blueprints/Creatures/Mite/Dust/BP_Mite_Dust.uasset.BP_Mite_Dust_C"
	,'Fire Soldier Ant':"summon /Game/Blueprints/Creatures/Ant/Fire/Soldier/BP_Ant_Soldier_Fire.uasset.BP_Ant_Soldier_Fire_C"
	,'Fire Worker Ant':"summon /Game/Blueprints/Creatures/Ant/Fire/Worker/BP_Ant_Fire.uasset.BP_Ant_Fire_C"
	,'Green Shield Bug':"summon /Game/Blueprints/Creatures/StinkBug/Upperyard/BP_StinkBug_Upperyard.uasset.BP_StinkBug_Upperyard_C"
	,'Hedge Broodmother':"summon /Game/Blueprints/Creatures/Spider/Boss01/BP_Spider_Boss_Hedge.uasset.BP_Spider_Boss_Hedge_C"
	,'Infected Gnat':"summon /Game/Blueprints/Creatures/Gnat/Infected/BP_Gnat_Infected.uasset.BP_Gnat_Infected_C"
	,'Infected Ladybug':"summon /Game/Blueprints/Creatures/Ladybug/Infected/BP_Ladybug_Infected.uasset.BP_Ladybug_Infected_C"
	,'Infected Larva':"summon /Game/Blueprints/Creatures/Larva/Infected/BP_Larva_infected.uasset.BP_Larva_infected_C"
	,'Infected Weavil':"summon /Game/Blueprints/Creatures/Weevil/Infected/BP_Weevil_Evil.uasset.BP_Weevil_Evil_C"
	,'Infected Wolf Spider':"summon /Game/Blueprints/Creatures/Spider/Wolf/BP_Spider_Wolf_Infected.uasset.BP_Spider_Wolf_Infected_C"
	,'Ladybird':"summon /Game/Blueprints/Creatures/Ladybug/Variants/BP_Ladybug_Upperyard.uasset.BP_Ladybug_Upperyard_C"
	,'Ladybird Larva':"summon /Game/Blueprints/Creatures/Larva/Charcoal/BP_Larva_Charcoal.uasset.BP_Larva_Charcoal_C"
	,'Larva':"summon /Game/Blueprints/Creatures/Larva/Base/BP_Larva.uasset.BP_Larva_C"
	,'Lawn Mite':"summon /Game/Blueprints/Creatures/Mite/Base/BP_Mite.uasset.BP_Mite_C"
	,'Mant':"summon /Game/Blueprints/Creatures/Mant/BP_Mant.uasset.BP_Mant_C"
	,'Mantis':"summon /Game/Blueprints/Creatures/Mantis/BP_Mantis.uasset.BP_Mantis_C"
	,'Mosquito':"summon /Game/Blueprints/Creatures/Mosquito/Base/BP_Mosquito.uasset.BP_Mosquito_C"
	,'Orb Weaver':"summon /Game/Blueprints/Creatures/Spider/OrbWeaver/BP_Spider_Web.uasset.BP_Spider_Web_C"
	,'Orb Weaver Jr.':"summon /Game/Blueprints/Creatures/Spider/Small/BP_Spider_Small.uasset.BP_Spider_Small_C"
	,'RUZ.T':"summon /Game/Blueprints/Creatures/TazT/TaserMelee/BP_TazT_Rusty.uasset.BP_TazT_Rusty_C"
	,'Red Soldier Ant':"summon /Game/Blueprints/Creatures/Ant/Red/Soldier/BP_Ant_Soldier.uasset.BP_Ant_Soldier_C"
	,'Spiderling':"summon /Game/Blueprints/Creatures/Spider/Spiderling/BP_Spiderling.uasset.BP_Spiderling_C"
	,'Spiny Water Flea':"summon /Game/Blueprints/Creatures/WaterFlea/Upperyard/BP_WaterFlea_UpperYard.uasset.BP_WaterFlea_UpperYard_C"
	,'Stinkbug':"summon /Game/Blueprints/Creatures/StinkBug/Base/BP_StinkBug.uasset.BP_StinkBug_C"
	,'TAYZ.T':"summon /Game/Blueprints/Creatures/TazT/TaserMelee/BP_TazT.uasset.BP_TazT_C"
	,'Termite King':"summon /Game/Blueprints/Creatures/Termite/King/BP_Termite_King.uasset.BP_Termite_King_C"
	,'Termite Soldier':"summon /Game/Blueprints/Creatures/Termite/Base/BP_Termite_Soldier.uasset.BP_Termite_Soldier_C"
	,'Termite Worker':"summon /Game/Blueprints/Creatures/Termite/Base/BP_Termite_Worker.uasset.BP_Termite_Worker_C"
	,'Tick':"summon /Game/Blueprints/Creatures/Mite/Tick/BP_Mite_Tick.uasset.BP_Mite_Tick_C"
	,'Tiger Mosquito':"summon /Game/Blueprints/Creatures/Mosquito/Variant/BP_Mosquito_Tiger.uasset.BP_Mosquito_Tiger_C"
	,'Water Flea':"summon /Game/Blueprints/Creatures/WaterFlea/Base/BP_WaterFlea.uasset.BP_WaterFlea_C"
	,'Wolf Spider':"summon /Game/Blueprints/Creatures/Spider/Wolf/BP_Spider_Wolf.uasset.BP_Spider_Wolf_C"
	,'Aphid':"summon /Game/Blueprints/Creatures/Aphid/Base/BP_Aphid.uasset.BP_Aphid_C"
	,'Gnat':"summon /Game/Blueprints/Creatures/Gnat/Base/BP_Gnat.uasset.BP_Gnat_C"
	,'Grub':"summon /Game/Blueprints/Creatures/Grub/Base/BP_Grub.uasset.BP_Grub_C"
	,'Meaty Gnat':"summon /Game/Blueprints/Creatures/Gnat/Base/BP_Gnat_Big.uasset.BP_Gnat_Big_C"
	,'Scarab':"summon /Game/Blueprints/Creatures/CrystalBeetle/BP_CrystalBeetle.uasset.BP_CrystalBeetle_C"
	,'Tadpole':"summon /Game/Blueprints/Creatures/Tadpole/Base/BP_Tadpole.uasset.BP_Tadpole_C"
	,'Water Boatman':"summon /Game/Blueprints/Creatures/Water_Boatman/Base/BP_WaterBoatman.uasset.BP_WaterBoatman_C"
	,'Weevil':"summon /Game/Blueprints/Creatures/Weevil/Base/BP_Weevil.uasset.BP_Weevil_C"
	,'Mighty Jewel':"summon /Game/Blueprints/Items/World/Crafted/BP_World_Jewel_Quartzite.uasset.BP_World_Jewel_Quartzite_C"
	,'Mint Jewel':"summon /Game/Blueprints/Items/World/Crafted/BP_World_Jewel_Mint.uasset.BP_World_Jewel_Mint_C"
	,'Salt Jewel':"summon /Game/Blueprints/Items/World/Crafted/BP_World_Jewel_Salt.uasset.BP_World_Jewel_Salt_C"
	,'Sour Jewel':"summon /Game/Blueprints/Items/World/Crafted/BP_World_Jewel_Sour.uasset.BP_World_Jewel_Sour_C"
	,'Spicy Jewel':"summon /Game/Blueprints/Items/World/Crafted/BP_World_Jewel_Spicy.uasset.BP_World_Jewel_Spicy_C"
	,'Mighty Glob':"summon /Game/Blueprints/Items/World/Crafted/BP_World_Ingot_Quartzite.uasset.BP_World_Ingot_Quartzite_C"
	,'Mint Glob':"summon /Game/Blueprints/Items/World/Crafted/BP_World_Ingot_Mint.uasset.BP_World_Ingot_Mint_C"
	,'Salt Glob':"summon /Game/Blueprints/Items/World/Crafted/BP_World_Ingot_Salt.uasset.BP_World_Ingot_Salt_C"
	,'Sour Glob':"summon /Game/Blueprints/Items/World/Crafted/BP_World_Ingot_Sour.uasset.BP_World_Ingot_Sour_C"
	,'Spicy Glob':"summon /Game/Blueprints/Items/World/Crafted/BP_World_Ingot_Spicy.uasset.BP_World_Ingot_Spicy_C"
	,'Brittle Whetstone':"summon /Game/Blueprints/Items/World/Crafted/BP_World_Weapon_Upgrade_Whetstone1.uasset.BP_World_Weapon_Upgrade_Whetstone1_C"
	,'Supreme Plating':"summon /Game/Blueprints/Items/World/Crafted/BP_World_Armor_Upgrade_Plate3.uasset.BP_World_Armor_Upgrade_Plate3_C"
	,'Sturdy Plating':'summon /Game/Blueprints/Items/World/Crafted/BP_World_Armor_Upgrade_Plate2.uasset.BP_World_Armor_Upgrade_Plate2_C'
	,'Brittle Plating':'summon /Game/Blueprints/Items/World/Crafted/BP_World_Armor_Upgrade_Plate1.uasset.BP_World_Armor_Upgrade_Plate1_C'
	,'Boost Juice':"summon /Game/Blueprints/Items/World/Crafted/Consumables/BP_World_Smoothie_Aphid_Sticky.uasset.BP_World_Smoothie_Aphid_Sticky_C"
	,'Fluid Flippers':"summon /Game/Blueprints/Items/World/Crafted/Consumables/BP_World_Smoothie_SwimSpeed_Sticky.uasset.BP_World_Smoothie_SwimSpeed_Sticky_C"
	,'Fuzz on the Rocks':"summon /Game/Blueprints/Items/World/Crafted/Consumables/BP_World_Smoothie_FuzzOnTheRocks_Sticky.uasset.BP_World_Smoothie_FuzzOnTheRocks_Sticky_C"
	,'Gastro Goo':'summon /Game/Blueprints/Items/World/Crafted/Consumables/BP_World_Smoothie_GastroGoo_Sticky.uasset.BP_World_Smoothie_GastroGoo_Sticky_C'
	,'Green Machine':"summon /Game/Blueprints/Items/World/Crafted/Consumables/BP_World_Smoothie_Fiber_Sticky.uasset.BP_World_Smoothie_Fiber_Sticky_C"
	,'Hedge Lord':"summon /Game/Blueprints/Items/World/Crafted/Consumables/BP_World_Smoothie_Berry_Sticky.uasset.BP_World_Smoothie_Berry_Sticky_C"
	,'Human Food':"summon /Game/Blueprints/Items/World/Crafted/Consumables/BP_World_Smoothie_HumanFood_Sticky.uasset.BP_World_Smoothie_HumanFood_Sticky_C"
	,'Liquid Gills':"summon /Game/Blueprints/Items/World/Crafted/Consumables/BP_World_Smoothie_WaterBreathing_Sticky.uasset.BP_World_Smoothie_WaterBreathing_Sticky_C"
	,'Liquid Rage':"summon /Game/Blueprints/Items/World/Crafted/Consumables/BP_World_Smoothie_Attack_Sticky.uasset.BP_World_Smoothie_Attack_Sticky_C"
	,'Questionable Slop':"summon /Game/Blueprints/Items/World/Crafted/Consumables/BP_World_Smoothie_Default_Sticky.uasset.BP_World_Smoothie_Default_Sticky_C"
	,"Worker's Comp":"summon /Game/Blueprints/Items/World/Crafted/Consumables/BP_World_Smoothie_Ant_Sticky.uasset.BP_World_Smoothie_Ant_Sticky_C"
	,'Black Ox Burger':"summon /Game/Blueprints/Items/World/Crafted/Consumables/Meals/BP_World_Meal_BlackOxBurger.uasset.BP_World_Meal_BlackOxBurger_C"
	#,'Boatman Fin Soup':"summon /blueprints/world/creatures/bee.uasset.bee_C"
	,'Funguspacho':"summon /Game/Blueprints/Items/World/Crafted/Consumables/Meals/BP_World_Meal_Funguspacho.uasset.BP_World_Meal_Funguspacho_C"
	,'Gnatchos':"summon /Game/Blueprints/Items/World/Crafted/Consumables/Meals/BP_World_Meal_Gnatchos.uasset.BP_World_Meal_Gnatchos_C"
	,'Larvagna':"summon /Game/Blueprints/Items/World/Crafted/Consumables/Meals/BP_World_Meal_Larvagna.uasset.BP_World_Meal_Larvagna_C"
	,'Mac N Bees':"summon /Game/Blueprints/Items/World/Crafted/Consumables/Meals/BP_World_Meal_MacNBees.uasset.BP_World_Meal_MacNBees_C"
	,'Miteloaf':"summon /Game/Blueprints/Items/World/Crafted/Consumables/Meals/BP_World_Meal_Miteloaf.uasset.BP_World_Meal_Miteloaf_C"
	,'Omelant':"summon /Game/Blueprints/Items/World/Crafted/Consumables/Meals/BP_World_Meal_Omelant.uasset.BP_World_Meal_Omelant_C"
	,'Quesadillantlion':"summon /Game/Blueprints/Items/World/Crafted/Consumables/Meals/BP_World_Meal_Quesadillantlion.uasset.BP_World_Meal_Quesadillantlion_C"
	,'Spaghetflea':"summon /Game/Blueprints/Items/World/Crafted/Consumables/Meals/BP_World_Meal_Spaghetflea.uasset.BP_World_Meal_Spaghetflea_C"
	,'Spider Slider':"summon /Game/Blueprints/Items/World/Crafted/Consumables/Meals/BP_World_Meal_SpiderSlider.uasset.BP_World_Meal_SpiderSlider_C"
	,'Tadpoloca Pudding':"summon /Game/Blueprints/Items/World/Crafted/Consumables/Meals/BP_World_Meal_TadpolePudding.uasset.BP_World_Meal_TadpolePudding_C"
	,'Termite Delight':"summon /Game/Blueprints/Items/World/Crafted/Consumables/Meals/BP_World_Meal_TermiteDelight.uasset.BP_World_Meal_TermiteDelight_C"
	,'Broodmother BLT':"summon /Game/Blueprints/Items/World/Crafted/Keys/BP_World_BossKey_Broodmother.uasset.BP_World_BossKey_Broodmother_C"
	,'Orchid Mantis Kebab':"summon /Game/Blueprints/Items/World/Crafted/Keys/BP_World_BossKey_Mantis.uasset.BP_World_BossKey_Mantis_C"
	,'Berry Leather':"summon /Game/Blueprints/Items/World/Crafted/BP_World_Fabric.uasset.BP_World_Fabric_C"
	,'Berry Chunk':'summon /Game/Blueprints/Items/World/BP_World_Hedge_Berry.uasset.BP_World_Hedge_Berry_C'
	,'Bomb, Sticky':"summon /Game/Blueprints/Items/World/Crafted/BP_World_T3Bomb_Sticky.uasset.BP_World_T3Bomb_Sticky_C"
	,'EverChar Coal Chunk':"summon /Game/Blueprints/Items/World/BP_World_Charcoal_Chunk.uasset.BP_World_Charcoal_Chunk_C"
	,'Lint Rope':"summon /Game/Blueprints/Items/World/Crafted/BP_World_LintWoven.uasset.BP_World_LintWoven_C"
	,'Pebblet':"summon /Game/Blueprints/Items/World/BP_World_Stone_Pebble.uasset.BP_World_Stone_Pebble_C"
	,'Pond Moss':"summon /Game/Blueprints/Items/World/BP_World_Pond_Moss.uasset.BP_World_Pond_Moss_C"
	,'Pupa Hide':"summon /Game/Blueprints/Items/World/BP_World_Pupa_Hide.uasset.BP_World_Pupa_Hide_C"
	,'Pupa Leather':"summon /Game/Blueprints/Items/World/Crafted/BP_World_Leather_Pupa.uasset.BP_World_Leather_Pupa_C"
	,'Spider Silk':"summon /Game/Blueprints/Items/World/Crafted/BP_World_WebWoven.uasset.BP_World_WebWoven_C"
	,'Toenail':"summon /Game/Blueprints/Items/World/BP_World_Toenail.uasset.BP_World_Toenail_C"
	,'Biomedical Badge':"summon /Game/Blueprints/Items/World/Crafted/Accessories/BP_World_Accessory_OminentLuggage.uasset.BP_World_Accessory_OminentLuggage_C"
	,'Broodmother Trinket':"summon /Game/Blueprints/Items/World/Crafted/Accessories/BP_World_Accessory_Broodmother.uasset.BP_World_Accessory_Broodmother_C"
	,'Compliance Badge':"summon /Game/Blueprints/Items/World/Crafted/Accessories/BP_World_Accessory_OminentLegal.uasset.BP_World_Accessory_OminentLegal_C"
	,'Defense Badge':"summon /Game/Blueprints/Items/World/Crafted/Accessories/BP_World_Accessory_OminentCustomerSatisfaction.uasset.BP_World_Accessory_OminentCustomerSatisfaction_C"
	,'Entomologist Badge':"summon /Game/Blueprints/Items/World/Crafted/Accessories/BP_World_Accessory_OminentOfficeSupplies.uasset.BP_World_Accessory_OminentOfficeSupplies_C"
	,'Everlasting Hogstopper':"summon /Game/Blueprints/Items/World/Crafted/Accessories/BP_World_Accessory_Hotdog.uasset.BP_World_Accessory_Hotdog_C"
	,'Fluffy Dandelion Tuft':"summon /Game/Blueprints/Items/World/Harvested/BP_World_Dandelion_Puff_Pristine.uasset.BP_World_Dandelion_Puff_Pristine_C"
	,'Fungal Charm':"summon /Game/Blueprints/Items/World/Crafted/Accessories/BP_World_Accessory_ExplosiveFungus.uasset.BP_World_Accessory_ExplosiveFungus_C"
	,'Hot Cha Charm':"summon /Game/Blueprints/Items/World/Crafted/Accessories/BP_World_Accessory_Spicy.uasset.BP_World_Accessory_Spicy_C"
	,'Insulating Larva Spike':"summon /Game/Blueprints/Items/World/Crafted/Accessories/BP_World_Accessory_Larva.uasset.BP_World_Accessory_Larva_C"
	,'Intern Badge':"summon /Game/Blueprints/Items/World/Crafted/Accessories/BP_World_Accessory_OminentMouthFeel.uasset.BP_World_Accessory_OminentMouthFeel_C"
	,'Left Elf Charm':"summon /Game/Blueprints/Items/World/Crafted/Accessories/BP_World_Accessory_LeftHalf.uasset.BP_World_Accessory_LeftHalf_C"
	,'Mantis Trinket':"summon /Game/Blueprints/Items/World/Crafted/Accessories/BP_World_Accessory_Mantis.uasset.BP_World_Accessory_Mantis_C"
	,'Power Droplet':"summon /Game/Blueprints/Items/World/Crafted/Accessories/BP_World_Accessory_Unarmed.uasset.BP_World_Accessory_Unarmed_C"
	,'Right Elf Charm':"summon /Game/Blueprints/Items/World/Crafted/Accessories/BP_World_Accessory_RightHalf.uasset.BP_World_Accessory_RightHalf_C"
	,'Rotten Berry Charm':"summon /Game/Blueprints/Items/World/Crafted/Accessories/BP_World_Accessory_Rotten.uasset.BP_World_Accessory_Rotten_C"
	,"Serah's Charm":"summon /Game/Blueprints/Items/World/Crafted/Accessories/BP_World_Accessory_CombinedHalves.uasset.BP_World_Accessory_CombinedHalves_C"
	,'Shiny Salt Crystal':"summon /Game/Blueprints/Items/World/Crafted/Accessories/BP_World_Accessory_Salty.uasset.BP_World_Accessory_Salty_C"
	,'Suspicious Ice Cap':"summon /Game/Blueprints/Items/World/Crafted/Accessories/BP_World_Accessory_Fresh.uasset.BP_World_Accessory_Fresh_C"
	,"Thor's Pendant":"summon /Game/Blueprints/Items/World/Crafted/Accessories/BP_World_Accessory_Pendant.uasset.BP_World_Accessory_Pendant_C"
	,'Toxicology Badge':"summon /Game/Blueprints/Items/World/Crafted/Accessories/BP_World_Accessory_OminentHouseCleaning.uasset.BP_World_Accessory_OminentHouseCleaning_C"
	,'Wonderous Wormhole':"summon /Game/Blueprints/Items/World/Crafted/Accessories/BP_World_Accessory_Sour.uasset.BP_World_Accessory_Sour_C"
	,'Build All Buildings':"BuildAllBuildings"
	,'Repair All Items':"RepairAllItems"
	,'Full Restore':"FullRestore"
	,'God Mode':"god"
	,'Infinite Damage':"InfiniteDamage"
	,'Boost/Fuzz/Green/Rage Smoothies':"summon /Game/Blueprints/Items/World/Crafted/Consumables/BP_World_Smoothie_Aphid_Sticky.uasset.BP_World_Smoothie_Aphid_Sticky_C|summon /Game/Blueprints/Items/World/Crafted/Consumables/BP_World_Smoothie_FuzzOnTheRocks_Sticky.uasset.BP_World_Smoothie_FuzzOnTheRocks_Sticky_C|summon /Game/Blueprints/Items/World/Crafted/Consumables/BP_World_Smoothie_Fiber_Sticky.uasset.BP_World_Smoothie_Fiber_Sticky_C|summon /Game/Blueprints/Items/World/Crafted/Consumables/BP_World_Smoothie_Attack_Sticky.uasset.BP_World_Smoothie_Attack_Sticky_C"
	,"Bomb Arrow":"summon /Game/Blueprints/Items/World/Crafted/BP_World_Arrow_Splinter_Bomb.uasset.BP_World_Arrow_Splinter_Bomb_C"
	,"Sour Arrow":"summon /Game/Blueprints/Items/World/Crafted/BP_World_Arrow_Sour.uasset.BP_World_Arrow_Sour_C"
	,"Super Venom Arrow":"summon /Game/Blueprints/Items/World/Crafted/BP_World_Arrow_Splinter_Poison.uasset.BP_World_Arrow_Splinter_Poison_C"
	,"Splinter Arrow":"summon /Game/Blueprints/Items/World/Crafted/BP_World_Arrow_Splinter.uasset.BP_World_Arrow_Splinter_C"}

root = Tk()
#root.iconbitmap("icon_IvG_icon.ico")
root.title("Grounded Console Commands")
root.resizable(False, False)
root.geometry("800x180")

dropdown_frame = ttk.Frame(root)

catefory_frame = ttk.Frame(dropdown_frame)
category_lbl = ttk.Label(catefory_frame, text="Select Category:")
category_lbl.pack(pady=(0,3))

category_type = StringVar()
categorycb=ttk.Combobox(catefory_frame,width=30, textvariable=category_type)
categorycb['values']=category_drop
categorycb['state']='readonly'
categorycb.current(0)
categorycb.pack(padx=5,side=LEFT)
catefory_frame.pack(side=LEFT)

selection_frame=ttk.Frame(dropdown_frame)

category_lbl = ttk.Label(selection_frame, text="Select Blueprint:")
category_lbl.pack(pady=(0,3))

selection_type = StringVar()	

selectionCombo= ttk.Combobox(selection_frame, width=60, textvariable=selection_type, postcommand=category_select_match)
selectionCombo['state']='readonly'
selectionCombo.pack(padx=5)

selectionCombo.bind("<<ComboboxSelected>>", callback)

selection_frame.pack()
dropdown_frame.pack(pady=(5,0))

blueprint_lbl = ttk.Label(root, text="Sample Console Command")
blueprint_lbl.pack(pady=(10,0))

sample_frame = ttk.Frame(root)
sample=StringVar()
sample_entry = ttk.Entry(master=sample_frame, width = 120, state='readonly',justify=CENTER, textvariable=sample)
sample_entry.pack(side=LEFT)

sample_frame.pack(pady=(5,5))

quantity_frame = ttk.Frame(root)

quantity_lbl = ttk.Label(quantity_frame, text="Quantity: ")
quantity_lbl.pack(side=LEFT)

quantity_entry = ttk.Entry(master=quantity_frame,justify=CENTER, width=10)
quantity_entry.insert(0,1)
quantity_entry.pack(pady=(3,0))

quantity_frame.pack()

copy_button = ttk.Button(master=root,width=20,text="Copy to Clipboard",command=copy_final)
copy_button.pack(pady=(10,0))

root.mainloop()