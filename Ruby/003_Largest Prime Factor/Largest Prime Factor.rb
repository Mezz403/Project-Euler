require "benchmark"
require "prime"

print "Enter number: "
number = gets.chomp.to_i

primes = []

time = Benchmark.realtime do
	prime_factors = Prime.prime_division(number)
	prime_factors.each { |prime,exponent| primes << prime }

	puts primes.max
end

puts "Time elapsed #{time*1000} milliseconds"