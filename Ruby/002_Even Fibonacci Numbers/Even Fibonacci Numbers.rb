require "benchmark"

print "Enter limit: "
limit = gets.chomp.to_i

fib_n1 = 0
fib_n2 = 1
fib_n = 0
arr_fib = []
sum = 0

time = Benchmark.realtime do
	until (fib_n1 + fib_n2) > limit do
		fib_n = fib_n1 + fib_n2
		arr_fib << fib_n
		fib_n1 = fib_n2
		fib_n2 = fib_n
	end

	for num in arr_fib
		if num.even?
			sum += num
		end
	end

	puts sum
end

puts "Time elapsed #{time*1000} milliseconds"