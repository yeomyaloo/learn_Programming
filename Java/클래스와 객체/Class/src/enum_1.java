
public class enum_1 {
	public static final String MALE ="MALE";
	public static final String FEMALE ="FEMALE";
	public static void main(String[] args) {
		// ����Ÿ���� �����ؼ� ���� ������ �� ����Ÿ������ ����� �� �ִ�.
		String gender1;
		gender1 = enum_1.MALE;
		gender1 = enum_1.FEMALE;
		//�� ���� Ÿ���� �ְ� ������ ���� �Ǹ��� �̿��� �ٸ� ��Ʈ�� Ÿ���� �� �� �ִ� �̴� �����Ͽ��� ������ ������ ������ �� �̿ܿ� ������ ���ܹ�����.
		gender1 = "boy"; //�̷��� �ٸ� ��Ʈ���� �� �� �־ �̸� �����ϱ� ���� ������ ����Ѵ�.
		
		
		
		Gender gender2;
		gender2 = Gender.MALE;
		gender2 = Gender.FEMALE;
//		gender2 = Gender.boy;  �����Ϻ��� ������ ��Ÿ����.
		

	}

}
enum Gender{
	MALE, FEMALE;
}