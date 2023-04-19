from typing import List, Tuple
import math


def surf_and_graph(data:List[Tuple[float,float,float]], scale:float=0.0)->Tuple[Tuple[List[float],List[float]], Tuple[List[float],List[float]]]:
	graph_points = _get_points(data,scale)
	return __xy_coords(data), __xy_coords(graph_points)


def __xy_coords(data:List[Tuple[float,float,float]]|List[Tuple[float,float]], scale:float=0.0)->Tuple[List[float],List[float]]:
	x = [p[0] for p in data]
	y = [p[1] for p in data]
	# append the first point to the end to ensure closed curve
	x.append(x[0])
	y.append(y[0])

	coords = (x,y)
	return coords


def _get_points(data:List[Tuple[float,float,float]], scale:float=0.0)->List[Tuple[float,float]]:
	"""data items represent an x and y coordinate and value of some quantity at the x,y coordinates."""

	scaling_factor = 1.0
	if scale!=0:
		geom_scale, value_scale = __geometry_and_values_scale(data)
		if value_scale>0:
			scaling_factor = scale*geom_scale/value_scale

	graph = list()
	K = len(data)-1
	k,l = K,0

	e = _e_vector(data[k],data[l])
	e0 = e

	while l<K:
		k = l
		l += 1
		e_old = e
		e = _e_vector(data[k],data[l])
		n = _get_normal(e_old,e)
		scaled_value = data[k][2]*scaling_factor
		graph.append(
			(data[k][0]+n[0]*scaled_value, data[k][1]+n[1]*scaled_value)
		)
	e_old = e

	n = _get_normal(e_old,e0)
	scaled_value = data[K][2]*scaling_factor
	graph.append(
		(data[K][0]+n[0]*scaled_value, data[K][1]+n[1]*scaled_value)
	)
	return graph


def __geometry_and_values_scale(data:List[Tuple[float,float,float]])->Tuple[float,float]:
	values = [p[2] for p in data]
	x = [p[0] for p in data]
	y = [p[1] for p in data]
	geom_scale = max(max(x)-min(x), max(y)-min(y))
	value_scale = max(abs(max(values)),abs(min(values)))
	return geom_scale, value_scale


def _e_vector(pointA:Tuple[float,float,float],pointB:Tuple[float,float,float])->Tuple[float,float]:
	px,py = pointB[0]-pointA[0], pointB[1]-pointA[1]
	p = math.sqrt(px*px + py*py)
	return px/p, py/p


def __dot(u:Tuple[float,float],v:Tuple[float,float])->float:
	return u[0]*v[0]+u[1]*v[1]


def _get_normal(e_old:Tuple[float,float], e:Tuple[float,float])->List[float]:
	if __dot(e, e_old)>0: 
		mx = e[1]+e_old[1]
		my = -(e[0]+e_old[0])
	else:
		mx = e_old[0]-e[0]
		my = e_old[1]-e[1]
	m = math.sqrt(mx*mx + my*my)
	return [mx/m, my/m]
	
