from num2words import num2words as n2w

print("*** Sing Along ***")

print("\n".join(["""%s green bottles hanging on the wall,
%s green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There'll be %s green bottles hanging on the wall."""
	% (n2w(i+1).title(), n2w(i+1).title(), n2w(i)) for i in range(int(input("Range: ")))[::-1]]))  # Technically 1 line
