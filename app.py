"""Flask application that provides an overview of Presbyterian Church of Korea (Tonghap) systematic theology."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List

from flask import Flask, jsonify, render_template


app = Flask(__name__)


@dataclass
class TheologySection:
    """Representation of a theology content section."""

    title: str
    summary: str
    bullet_points: List[str]


THEOLOGY_CONTENT: Dict[str, TheologySection] = {
    "foundations": TheologySection(
        title="역사적 배경과 신학적 기초",
        summary=(
            "대한예수교장로회 통합측은 1953년 분립 이후 화해와 선교, 그리고 공적 책임을 강조하는"
            " 장로교 전통 위에서 체계신학을 발전시켜 왔습니다. 통합측은 칼빈주의 전통을 유지하면서도"
            " 한국 사회의 역사적 아픔과 변화를 신학적으로 성찰하고 응답하는 것을 중요하게 여깁니다."
        ),
        bullet_points=[
            "웨스트민스터 신앙고백과 대·소요리문답을 핵심 신조로 수용",
            "칼빈과 바르트 신학을 비판적으로 계승하면서도 에큐메니컬 운동에 적극 참여",
            "신학 교육과 교회의 공적 역할을 강조",
        ],
    ),
    "revelation": TheologySection(
        title="계시와 성경 이해",
        summary=(
            "통합측 체계신학은 하나님이 성경을 통해 자신을 드러내셨다는 전통적 계시 이해를 따르면서도,"
            " 성경 해석에 있어 역사비평과 문학적 방법을 수용하여 오늘의 삶에 적용하려는 실천적 해석학을"
            " 추구합니다."
        ),
        bullet_points=[
            "성경을 신앙과 행위의 유일한 법칙으로 고백",
            "신앙 공동체 안에서의 성령의 조명과 해석 공동체의 중요성 강조",
            "신학과 과학, 문화의 대화를 통해 해석을 갱신",
        ],
    ),
    "christology": TheologySection(
        title="그리스도론",
        summary=(
            "예수 그리스도는 통합측 신학에서 구속 역사와 하나님 나라 운동의 중심입니다."
            " 십자가와 부활의 사건을 통해 나타난 하나님 사랑의 보편성과,"
            " 사회적 약자와 함께하신 그리스도의 삶을 현대적 실천으로 연결합니다."
        ),
        bullet_points=[
            "그리스도의 삼중직(선지자, 제사장, 왕) 강조",
            "그리스도의 구속 사역을 개인 구원과 사회 변혁 모두로 확장",
            "에큐메니컬 맥락에서의 그리스도 이해를 수용",
        ],
    ),
    "ecclesiology": TheologySection(
        title="교회론",
        summary=(
            "통합측은 교회를 하나님 백성의 공동체로 이해하며, 공적 책임과 선교적 실천을 강조합니다."
            " 교회는 예배와 성례, 말씀 선포를 통해 세상을 섬기는 선교적 공동체가 되어야 한다고 봅니다."
        ),
        bullet_points=[
            "장로회 정치 체계를 유지하며 신앙 공동체의 민주성과 질서 강조",
            "여성 안수 허용과 같은 포용적 정책을 통해 정의와 평등 지향",
            "사회 정의, 인권, 평화 운동에 적극 참여",
        ],
    ),
    "ethics": TheologySection(
        title="윤리와 사회 참여",
        summary=(
            "통합측 조직신학은 신앙과 삶의 통합을 강조하며, 정의와 평화, 생명 존중을 실천하는 공적 신앙을"
            " 제시합니다."
        ),
        bullet_points=[
            "기후 위기, 평화, 통일 문제에 대한 신학적 대응",
            "사회적 약자와 함께하는 섬김과 나눔 실천",
            "민주주의 발전과 인권 수호를 위한 목소리",
        ],
    ),
}


@app.get("/")
def index() -> str:
    """Render the main page with theology content."""

    return render_template("index.html", sections=THEOLOGY_CONTENT)


@app.get("/api/sections")
def sections() -> str:
    """Provide theology content as JSON."""

    return jsonify({key: section.__dict__ for key, section in THEOLOGY_CONTENT.items()})


if __name__ == "__main__":
    app.run(debug=True)
