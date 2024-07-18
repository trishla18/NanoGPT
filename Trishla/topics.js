topics = {"1":["Time Value of Money", "k"], "2":["Working Capital Management"], "3":["Capital Budgeting"], "4":["Capital Structure"], "5":["Something"], "6":["Something Else"]};
function populateTopics()
{
  const urlParams = new URLSearchParams(window.location.search);
  const subjectNo = urlParams.get("subject");
  if(subjectNo && topics.hasOwnProperty(subjectNo))
  {
    document.getElementsByClassName("schedule-container")[0].innerHTML = "<h2>TOPICS</h2>";
    topics[subjectNo.toString()].forEach((item)=>{
      document.getElementsByClassName("schedule-container")[0].innerHTML = document.getElementsByClassName("schedule-container")[0].innerHTML+ `<div class="schedule-item yellow">
        <div class="details">
          <h3>`+item+`</h3>
        </div>
        <button class="join-btn">Join</button>
      </div>`;
    });
  }
}
window.onload = populateTopics;