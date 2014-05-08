import java.util.Scanner;

public class Euler {
	public static void main(String[] args) {
		System.out.println("Answer to which problem?");

		Scanner s = new Scanner(System.in);
		int i = 0;
		boolean read = false;

		while (!read) {
			if (s.hasNext()) {
				i = s.nextInt();
				read = true;
			}
		}
		try {
			switch (i) {
			case 1:
				System.out.println(p1());
				break;
			case 2:
				System.out.println(p2());
				break;
			case 3:
				System.out.println(p3());
				break;
			case 4:
				System.out.println(p4());
				break;
			case 5:
				System.out.println(p5());
				break;
			case 6:
				System.out.println(p6());
				break;
			case 7:
				System.out.println(p7());
				break;
			case 8:
				System.out.println(p8());
				break;
			case 9:
				System.out.println(p9());
				break;
			default:
				throw new IndexOutOfBoundsException();
			}
		} catch (IndexOutOfBoundsException e) {
			System.out.println("Problem not solved.");
		}

	}

	private static int p1() {
		int sum = 0;
		for (int i = 1; i < 1000; i++) {
			if (i % 3 == 0 || i % 5 == 0)
				sum += i;
		}

		return sum;
	}

	private static int p2() {
		int beforePrev = 1;
		int prev = 2;
		
		int sum = 0;
		
		for (int i = beforePrev + prev; i < 4000000; i = beforePrev + prev) {
			if (i % 2 == 0)
				sum += i;
			beforePrev = prev;
			prev = i;
		}
		
		return sum;
	}

	private static int p3() {
		return 404;
	}

	private static int p4() {
		return 404;
	}

	private static int p5() {
		return 404;
	}

	private static int p6() {
		return 404;
	}

	private static int p7() {
		return 404;
	}

	private static int p8() {
		return 404;
	}

	private static int p9() {
		return 404;
	}

}
