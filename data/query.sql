SELECT DISTINCT f.name as "Product name", lab.name as "Lab name", n, p, k, mg, ca, s, zn, mn, fe, cu, b, al, organic_material, acidity
FROM fertilizer f, lab, fertilizer_lab f_l, nutrientset ns
WHERE f.name = '15-15-15' 
	AND f.nutrient_set = ns.id
	AND f.id = f_l.fertilizer
	AND lab.id = f_l.lab


