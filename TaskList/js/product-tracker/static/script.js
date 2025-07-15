let viewTimers = {};

function startTimer(el) {
  const id = el.dataset.id;
  viewTimers[id] = Date.now();
}

function endTimer(el) {
  const id = el.dataset.id;
  const start = viewTimers[id];
  if (!start) return;

  const viewTime = Date.now() - start;
  console.log("Sending view data for", id, viewTime);

  fetch('/api/track-view', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      productId: id,
      viewTime: viewTime
    })
  });
}

window.onload = function () {
  fetch('/api/recommendations')
    .then(res => res.json())
    .then(data => {
      const div = document.getElementById('recommendations');
      if (data.length === 0) {
        div.innerText = "No recommendations yet. Hover on products to track.";
      } else {
        div.innerHTML = data.map(p => `<strong>${p}</strong>`).join("<br>");
      }
    });
}
