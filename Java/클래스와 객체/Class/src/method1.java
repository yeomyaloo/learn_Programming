
public class method1 {

		// �ʵ尡 ��ü�� ���¶��, ��ü�� �ൿ�� �ش��ϴ°� �޼ҵ��. 
		//car�� �̸��� ��ȣ�� �ֱ⵵ ������, car�� ������ �����Ҽ��� �ְ� �����ϴ� �ൿ�� �� �� �ִ�.
		//�Է°� : �Ű�����(Parameter) �� � �Լ��� ȣ��ÿ� ���޵Ǵ� ���� �ǹ��Ѵ�.
		// ����(Argument)�� ���޵� ���ڸ� �޾Ƶ��̴� ������ �ǹ��Ѵ�.
		// ����� : ���ϰ�
		
		
		//�޼ҵ� ����(Ŭ������ ������ �ִ� ���)/ Ŭ���� ���ο� ������ �ȴ�.
		//public ����Ÿ�� �żҵ�� (�Ű����� ��){ �ʿ��� ���� }
		
		//�Ű�����, ���ϵ� ���� ����
		public void method1_1() {
			System.out.println("method1�� ����˴ϴ�.");
		}
		
		//�Ű����� 1�� ���ϰ��� ���� ����
		public void method1_2(int x) {
			System.out.println(x + "�� �̿��� method2�� ����˴ϴ�.");
		}
		
		//���ϰ��� int������ �ְ� �Ű������� ���� ����
		public int method1_3() {
			System.out.println("method3�� ����˴ϴ�..");
			return 10;
		}
		// ���ϰ��� ���� �Ű������� x, y�� �� �� �޾Ƶ��� ����
		public void method1_4(int x, int y) {
			System.out.println(x + y + "�� �̿��� method4�� ����˴ϴ�.");
		}
		
		//���� �޾Ƽ� ���� ����ϴ� ���� 
		public int method1_5(int y) {
			System.out.println( y + "�� �̿��� method5�� ����˴ϴ�.");
			return y*2;
		}
}
