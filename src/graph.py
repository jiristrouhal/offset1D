from typing import List, Tuple
import math


def _get_points(data:List[Tuple[float,float,float]])->List[Tuple[float,float]]:
	"""data items represent an x and y coordinate and value of some quantity at the x,y coordinates."""
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
		graph.append(
			(data[k][0]+n[0]*data[k][2], data[k][1]+n[1]*data[k][2])
		)
	e_old = e

	n = _get_normal(e_old,e0)
	graph.append(
		(data[K][0]+n[0]*data[K][2], data[K][1]+n[1]*data[K][2])
	)
	return graph


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
	
