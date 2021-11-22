def triangle(n, k):
	if n <= 0:
	  return

	triangle(n - 1, k)
	
	if n == k:
		stars = []
	if n < k:
		stars = [' '] * (k - n)
	stars += [' * '] * n
	print(*stars)

triangle(5, 5)
