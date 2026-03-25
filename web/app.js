async function getRec() {
    const userId = document.getElementById("user_id").value;
    const res = await fetch(`http://localhost:8000/recommend?user_id=${userId}`);
    const data = await res.json();

    const ul = document.getElementById("result");
    ul.innerHTML = "";

    data.recommendations.forEach(item => {
        const li = document.createElement("li");
        li.innerText = item;
        ul.appendChild(li);
    });
}