import { Yaldevi } from "next/font/google";
import myData from "../../ev_incentives_comparison.json"

export default async function Home() {
  
  

  const xAxis = myData.map((temp) => temp.amount);
  const yAxis = myData.map((temp) => temp.percent);

  return (
    <div>
      <ul>
        {myData.map((item, index) => (
          <li key={index}>
            Amount: {item.amount}, Percent: {item.percent}%
        </li>))}
      </ul>
      <h1 className="font-bold">WE ARE WINNING THIS!</h1>
      
    </div>


    


  );
}
 