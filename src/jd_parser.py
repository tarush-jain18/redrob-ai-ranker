from docx import Document

def load_jd(path):

    doc = Document(path)

    text = "\n".join(
        para.text
        for para in doc.paragraphs
    )

    return text


if __name__ == "__main__":

    jd = load_jd(
        "data/job_description.docx"
    )

    print(jd[:5000])