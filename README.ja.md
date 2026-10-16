🇰🇷 [한국어](README.md) · 🇺🇸 [English](README.en.md) · 🇯🇵 **日本語**

# 🐍 Pythonプログラミング基礎 (CLASS_PYTHON_START)

<p align="center">
  <a href="https://ldjwj.github.io/CLASS_PYTHON_START/README.ja.html">
    <img src="https://img.shields.io/badge/🌐_Web教材を開く-GitHub_Pages-2563EB?style=for-the-badge&logo=githubpages&logoColor=white" alt="Web Page"/>
  </a>
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+"/>
  <img src="https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white" alt="Jupyter"/>
  <img src="https://img.shields.io/badge/Google_Colab-Ready-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white" alt="Google Colab"/>
  <img src="https://img.shields.io/badge/License-CC_BY--NC_4.0-lightgrey.svg?style=for-the-badge" alt="License"/>
</p>

> **誰でも気軽に始められる、Pythonプログラミングの第一歩！**  
> Pythonの基本文法（変数、制御文、関数、クラス）から実践的な応用（住所録、ミニプロジェクト）、さらにデータ分析・AIの入門まで、段階的な実習コードを提供します。  
> ⭐️ 学習のお役に立てたなら、右上の **Star** ボタンをぜひ押してください！

> **ご注意：** 教材（PDF/HTML）はすべて **韓国語** で書かれています。コードはそのまま実行でき、HTMLページはブラウザ（Chromeなど）の自動翻訳で読むことができます。

<p align="center">
  <a href="#️-学習ロードマップ">🗺️ 学習ロードマップ</a> •
  <a href="#-python基礎文法の実習">📘 基礎文法</a> •
  <a href="#-python実践応用--プロジェクト">💡 実践応用</a> •
  <a href="#-データサイエンス--機械学習のお試し">📊 データ & AI入門</a> •
  <a href="#️-開発環境セットアップガイド">🛠️ 環境設定</a>
</p>

---

## 🗺️ 学習ロードマップ

```mermaid
flowchart TD
    subgraph Step1 ["Step 01. Python基礎文法をマスター"]
        A["Pythonを始めよう & データ型"] --> B["制御文 (if, for, while) & リスト"]
        B --> C["ファイル入出力 (File I/O)"]
        C --> D["関数、ラムダ & モジュール"]
        D --> E["オブジェクト指向プログラミング (Class)"]
    end

    subgraph Step2 ["Step 02. 実践応用 & ミニプロジェクト"]
        F["基本プログラミング実習<br>(九九、ページ数計算、例外処理、暗号化)"]
        G["住所録管理プログラムを作る"]
    end

    subgraph Step3 ["Step 03. データ分析 & AIの第一歩"]
        H["Seabornによるデータ可視化"]
        I["初めての機械学習モデル<br>(Tips、キノコデータセット)"]
        J["SQLiteデータベース連携"]
        K["AI応用 (QRコード、顔認識など)"]
    end

    E --> F --> G --> H --> I
    H --> J
    I --> K

    style Step1 fill:#EFF6FF,stroke:#3B82F6,stroke-width:1.5px
    style Step2 fill:#F0FDFA,stroke:#0D9488,stroke-width:1.5px
    style Step3 fill:#FEF3C7,stroke:#D97706,stroke-width:1.5px
```

---

## 📘 Python基礎文法の実習

すべての実習コードは、ブラウザからワンクリックで実行できる **Google Colab** 環境に対応しています。

| ステップ | 学習テーマ | 主な内容 | Colabでワンクリック実習 |
|:---:|:---|:---|:---:|
| **1-1** | **Pythonを始めよう** | 変数、データ型（数値、文字列）、基本的な入出力 `print()`、`input()` | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/LDJWJ/CLASS_PYTHON_START/blob/main/01_01_python_start.ipynb) |
| **1-2** | **条件文 & 繰り返し文 & リスト** | `if-else` による分岐、`for`/`while` による繰り返し、リストと辞書の操作 | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/LDJWJ/CLASS_PYTHON_START/blob/main/01_02_python_start_if_for_list.ipynb) |
| **1-3** | **ファイル入出力を学ぶ** | テキストファイルの読み書き（`open`、`with`、`readline`、`write`） | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/LDJWJ/CLASS_PYTHON_START/blob/main/01_03_python_start_file.ipynb) |
| **1-4** | **関数とモジュール** | ユーザー定義関数 `def`、引数と戻り値、標準モジュールの `import` | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/LDJWJ/CLASS_PYTHON_START/blob/main/01_04_python_start_fnc_module.ipynb) |
| **1-5** | **クラス（Class）入門** | クラスとオブジェクトの概念、`__init__` コンストラクタ、属性とメソッド | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/LDJWJ/CLASS_PYTHON_START/blob/main/01_04_class_start_typeA.ipynb) |
| **1-5** | **クラスの応用 & 継承** | クラスの継承、オーバーライド、オブジェクト指向のカプセル化 | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/LDJWJ/CLASS_PYTHON_START/blob/main/01_04_class_start_typeB.ipynb) |

---

## 💡 Python実践応用 & プロジェクト

学んだ理論をもとに、実際に動くプログラムを作ってみる実践パートです。

| チャプター | テーマ | 主な内容 | 教材・実習リンク |
|:---:|:---|:---|:---:|
| **2-1** | **基本的なプログラミング活用** | 九九の出力、掲示板の総ページ数の計算、エラー・例外処理（`try-except`）、文字列の暗号化 | [📄 PDF](https://ldjwj.github.io/CLASS_PYTHON_START/02_01_programming_2204.pdf) · [🌐 HTML](https://ldjwj.github.io/CLASS_PYTHON_START/02_01_programming_220413.html) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/LDJWJ/CLASS_PYTHON_START/blob/main/02_01_programming.ipynb) |
| **2-2** | **住所録管理プログラム** | ユーザーの登録・検索・修正・削除（CRUD）を行うコンソールアプリケーション | [📄 PDF](https://ldjwj.github.io/CLASS_PYTHON_START/02_02_python_start_contact_2204.pdf) · [💻 ソースコード](02_02_programming_contact.py) |

---

## 📊 データサイエンス & 機械学習のお試し

Pythonの文法を身につけた後、データ分析や人工知能の分野へ自然にステップアップするためのガイドです。

```
┌────────────────────────┐      ┌────────────────────────┐      ┌────────────────────────┐
│  📈 データ可視化        │ ---> │  🤖 機械学習モデリング  │ ---> │  💾 データベース連携    │
│  - Seaborn 基本チャート │      │  - Tips チップ予測回帰  │      │  - SQLite3 DB 接続      │
│  - データ分布の可視化   │      │  - キノコ毒性の分類予測 │      │  - テーブル作成/照会    │
└────────────────────────┘      └────────────────────────┘      └────────────────────────┘
```

* **📈 データ可視化 (Seaborn)**:
  * [📄 PDF教材](https://ldjwj.github.io/CLASS_PYTHON_START/03_01_Seaborn_Basic.pdf) · [🌐 HTMLビューア](https://ldjwj.github.io/CLASS_PYTHON_START/03_01_Seaborn_Basic.html)
* **🤖 機械学習モデルを作る (Scikit-Learn)**:
  * Tipsデータでチップを予測するランダムフォレスト: [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/LDJWJ/CLASS_PYTHON_START/blob/main/ch02_03_03_RandomForest_01_Tips_01.ipynb)
  * キノコ（Mushroom）の毒性を分類する初めてのモデル: [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/LDJWJ/CLASS_PYTHON_START/blob/main/03_02_ml_start.ipynb)
* **💾 SQLiteデータベース連携**:
  * PythonとSQLite3データベースの接続およびクエリの実行: [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/LDJWJ/CLASS_PYTHON_START/blob/main/03_03_DB.ipynb)
* **🎨 さまざまなPythonの活用**:
  * QRコード自動生成プログラム
  * AIお絵描き & 顔認識プログラムの体験

---

## 🛠️ 開発環境セットアップガイド

ローカルPC（Windows）で実習環境を構築するための詳細マニュアルです。

* **Anaconda（アナコンダ）インストールガイド**:
  * [📄 Anacondaインストール PDF](https://ldjwj.github.io/kagglebook/pdf_html/env01_anaconda_install_V11_2508.pdf)
* **Visual Studio Code（VS Code）のインストールとPython拡張機能の設定**:
  * [📄 VS Codeインストール PDF (1)](https://ldjwj.github.io/CLASS_PYTHON_START/03_[Window]01_visual_studio_code설치.pdf) · [🌐 HTML (1)](https://ldjwj.github.io/CLASS_PYTHON_START/03_[Window]01_visual_studio_code설치.html)
  * [📄 VS Codeインストール PDF (2)](https://ldjwj.github.io/CLASS_PYTHON_START/03_[Window]02_visual_studio_code설치(2).pdf) · [🌐 HTML (2)](https://ldjwj.github.io/CLASS_PYTHON_START/03_[Window]02_visual_studio_code설치(2).html)

---

## 🔗 ライセンスとお問い合わせ

* **お問い合わせ**: 著作権に関するお問い合わせ・その他の提携: [frontier1020@naver.com](mailto:frontier1020@naver.com)
* **ライセンス**: 本リポジトリのすべての資料は [CC BY-NC 4.0](LICENSE) ライセンスに従います。出典を明記すれば、非営利目的で自由にご利用いただけます。
