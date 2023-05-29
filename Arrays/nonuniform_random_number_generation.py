def nonuniform_random_number_generation(values:List[int], probabilities:List[float])->int:
	prefix_sum_of_probabilitites=list(itertools.accumulate(probabilities))
	interval_idx=bisect.bisect(prefix_sum_of_probabilitites, random.random())
	return values[interval_idx]

	#time complexity to compute a single value is O(n) which is the time to create the array intervals. this array also implies an O(n) space complexity
	#once the array is constructed, computinf each additional result entails in one call to the random number generator, followed by a binary search O(logn)