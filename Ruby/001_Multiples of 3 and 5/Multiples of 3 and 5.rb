require "Benchmark"

def mult_of_3(num)
	num % 3 == 0
end

def mult_of_5(num)
	num % 5 == 0
end

print("Enter limit:")
limit=gets.chomp.to_i

mults = []

time = Benchmark.realtime do
	for num in 1...limit
		if mult_of_3(num) || mult_of_5(num)
			mults << num
		end
	end

	sum = mults.inject(0){|sum, x| sum + x}
	puts sum
end

puts "Time elapsed #{time*1000} milliseconds"
