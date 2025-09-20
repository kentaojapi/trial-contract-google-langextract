import os
import pprint
import textwrap

import langextract as lx

INPUT_CONTRACT_TEXT = """
システム開発業務委託契約書

株式会社テクノロジーソリューションズ (以下「甲」という) と株式会社デジタルクリエイト (以下「乙」という) は、
Webアプリケーション開発業務委託に関し、以下の通り契約を締結する。

## 第1条（目的）
本契約は、甲が乙に委託するWebアプリケーション開発業務（以下「本件業務」という）に関する基本的事項を定めることを目的とする。

## 第2条（業務内容）
乙は甲に対し、顧客管理システムの設計、開発、テスト及び納品業務を行う。使用技術はReact、Node.js、PostgreSQLとする。

## 第3条（契約期間）
本契約の期間は、2025年2月1日から2025年8月31日までとする。ただし、両当事者の合意により延長することができる。

## 第4条（委託料）
甲は乙に対し、本件業務の対価として金500万円（税別）を支払う。支払方法は以下の通りとする。
- 着手金：契約締結時に150万円
- 中間金：中間納品時に200万円  
- 残金：最終納品時に150万円

## 第5条（支払条件）
各支払いは請求書受領後30日以内に、乙指定の銀行口座に振り込むものとする。振込手数料は甲の負担とする。

## 第6条（知的財産権）
本件業務により生じた成果物の著作権その他の知的財産権は、甲に帰属する。ただし、乙が既に有していた知的財産権は除く。

## 第7条（機密保持）
両当事者は、本契約に関連して知り得た相手方の機密情報を第三者に開示してはならない。この義務は契約終了後5年間継続する。

## 第8条（個人情報保護）
乙は、業務遂行中に取り扱う個人情報について、個人情報保護法その他関連法令を遵守し、適切に管理する。

## 第9条（禁止事項）
乙は以下の行為を禁止する。
1. 機密情報の目的外使用・第三者への開示
2. 反社会的勢力との一切の関係
3. 法令に違反する行為
4. 甲の信用を害する行為

## 第10条（反社会的勢力の排除）
両当事者は、自らが反社会的勢力でないこと、反社会的勢力と一切の関係を有しないことを表明し保証する。万が一、この表明に虚偽があった場合、相手方は直ちに本契約を解除できる。

## 第11条（納期）
乙は2025年8月15日までに成果物を甲に納品する。やむを得ない事由により納期の変更が必要な場合は、事前に甲の承諾を得る。

## 第12条（検収）
甲は納品後14日以内に検収を行い、結果を乙に通知する。期間内に通知がない場合は、検収完了とみなす。

## 第13条（瑕疵担保責任）
乙は納品後6ヶ月間、成果物の瑕疵について無償で修正する責任を負う。ただし、甲の仕様変更に起因する瑕疵は除く。

## 第14条（損害賠償）
いずれかの当事者が本契約に違反し、相手方に損害を与えた場合、違反当事者は相手方に対し、その損害を賠償する責任を負う。ただし、損害額の上限は本契約の委託料総額とする。

## 第15条（契約解除）
以下の場合、当事者は相手方に対し書面による通知をもって本契約を解除できる。
1. 相手方が本契約に重大な違反をし、催告後30日以内に是正されない場合
2. 相手方が反社会的勢力との関係を有することが判明した場合
3. 相手方が破産手続開始の申立てを受けた場合
4. その他、契約の継続が困難と認められる場合

---

契約締結日：2025年1月31日

甲：株式会社テクノロジーソリューションズ  
代表取締役　田中　一郎　印

乙：株式会社デジタルクリエイト  
代表取締役　佐藤　花子　印
"""


EXAMPLE_CONTRACT_TEXT = """
業務委託契約書
株式会社ハッチュウ（以下「甲」という）と株式会社ウケオイ（以下「乙」という）は、下記業務に関して、業務委託契約（以下「本契約」という）を締結する。

第１条（目的）
甲は、本契約の定めるところにより、下記業務を乙に委託し、乙はこれを受託する。
1. システム開発業務
2. システム運用業務

第２条（契約期間）
委託期間は、令和6年4月1日から令和10年3月31日までとする

第3条（委託料）
本契約に基づく乙の委託料は、5,000,000円とする。
支払は、銀行振込にて実施するものとする。

第4条（成果物の権利帰属）
委託業務により作成された成果物の、無体財産権及び有体物に関する一切の権利は、甲に帰
属する。

第５条（再委託の制限）
乙は、甲の書面による事前の承諾を得た場合を除き、本件業務を第三者に再委託してはなら
ない。

第６条（権利義務の譲渡）
甲および乙は、本契約により生ずる権利の全部または一部を、第三者に譲渡または引き受け
させてはならない。

第７条（秘密保持）
乙は、甲から秘密とされた本件業務に関する一切の情報を第三者に開示してはならない。

第８条（報告義務）
乙は、甲の求めがあるときは、委託業務に関する情報を速やかに報告しなければならない。

第９条（契約解除）
甲または乙が本契約の条項に違反したときは、当事者は何らの催告をせず、直ちに本契約の
全部または一部を解除し、また被った損害を請求することができる。

第１０条（不可抗力免責）
天才地変、戦争・内乱・暴動、法令の改廃・制定、公権力による命令・処分、労働争議、輸送機
関・通信回線の事故、為替の大幅な変動など、当事者の責めに帰すことのできない不可抗力に
よる契約の全部または一部の履行遅滞、履行不能または不完全履行については、当該当事者
は責任を負わない。

第１１条（管轄裁判所）
本契約に関し裁判上の紛争が生じたときには、甲の所在地を管轄する簡易裁判所または地方
裁判所を管轄裁判所とする。

第１２条（協議）
本契約で定めのない事項、並びに本契約の内容に変更が生じることとなった場合は、甲乙協
議のうえ、定めるものとする。
以上、本契約の成立を証するため、本書二通を作成し、署名捺印の上、各自一通を保有する。

令和6年3月1日
（甲） 住所 千葉県千葉市千葉町1丁目1番
名称 株式会社ハッチュウ
代表 発注 投太 印
（乙） 住所 埼玉県埼玉市埼玉町1丁目1番
名称 株式会社ウケオイ
代表 請負 勤 印
"""


class Extractor:
    JSONL_OUTPUT_PATH = "extraction_results.jsonl"

    def __init__(self) -> None:
        self.openai_api_key = os.environ["OPENAI_API_KEY"]

    @property
    def prompt(self):
        return textwrap.dedent("""
            "契約書の内容から以下の項目を抽出してください。
            - 契約書の締結日
            - 取引先（組織名）
            - NDA（秘密保持契約）が含まれているかどうか（True/False）
        """)

    @property
    def examples(self):
        return [
            lx.data.ExampleData(
                text=EXAMPLE_CONTRACT_TEXT,
                extractions=[
                    lx.data.Extraction(
                        extraction_class="execution_date",
                        extraction_text="令和6年3月1日",
                        attributes={
                            "execution_date_iso8601": "2024-03-01"
                        }
                    ),
                    lx.data.Extraction(
                        extraction_class="partner",
                        extraction_text="株式会社ハッチュウ",
                        attributes={
                            "partner_company_name": "株式会社ハッチュウ"
                        }
                    ),
                    lx.data.Extraction(
                        extraction_class="is_include_nda",
                        extraction_text="乙は、甲から秘密とされた本件業務に関する一切の情報を第三者に開示してはならない。",
                        attributes={
                            "is_include_nda": True
                        }
                    ),
                ]
            )
        ]

    def extract(self, text: str):
        result = lx.extract(
            text_or_documents=text,
            prompt_description=self.prompt,
            examples=self.examples,
            model_id="gpt-4.1",
            api_key=self.openai_api_key,
            fence_output=True,  # OpenAI使用時は必須
            use_schema_constraints=False  # OpenAIでは未実装
        )
        pprint.pprint(result)
        return result

    def save_results(self, result) -> None:
        lx.io.save_annotated_documents([result], output_name=self.JSONL_OUTPUT_PATH, output_dir=".")

    def create_visualization(self) -> None:
        html_content = lx.visualize(self.JSONL_OUTPUT_PATH)
        with open("visualization.html", "w") as f:
            if hasattr(html_content, 'data'):
                f.write(html_content.data)  # For Jupyter/Colab
            else:
                f.write(html_content)

    def run_all(self) -> None:
        result = self.extract(INPUT_CONTRACT_TEXT)
        self.save_results(result)
        self.create_visualization()


def main():
    extractor = Extractor()
    extractor.run_all()


if __name__ == "__main__":
    main()
