# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def two_sum(nums, target)
  hash = {}
  for i in 0..nums.length-1 do
    t = target - nums[i]
    if hash.key?(nums[i])
      return [i, hash[nums[i]]]
    else
      hash[t] = i
    end
  end
end

# other solutions actually construct the longest substring, which is somehow faster? not sure how that one works ngl
def length_of_longest_substring(s)
  ml = 0
  i = 0
  hash = {}
  len = 0
  while i < s.length

    if !hash[s[i]]
      hash[s[i]] = i
      len+=1
    else
      ml = [ml, len].max
      i = hash[s[i]]
      hash = {}
      len = 0
    end
    i += 1
  end
  return [len, ml].max
end

def is_valid(s)
  open = []
  valid = {
    '(' => ')',
    '[' => ']',
    '{' => '}',
  }
  s.each_char do |c|
    if valid.key?(c)
      open.append(c)
    elsif valid.value?(c)
      if valid[open.pop] != c
        return false
      end
    end
  end
  return open.empty?
end

puts "Hello world!"

puts is_valid("()")
puts is_valid("{()}")
puts is_valid("{{}")
puts is_valid("{}}")