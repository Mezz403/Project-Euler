require "benchmark"

print "Enter limit:"
limit = gets.chomp
palindromes = []

time = Benchmark.realtime do
	for i in 1..limit.to_i
		if  i.to_s.reverse == i.to_s
			palindromes << i
		end
	end

	puts palindromes.last

end

puts "Time elapsed #{time*1000} milliseconds"