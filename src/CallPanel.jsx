// Reactフロントエンド: 顧客情報と通話コントロール画面
import { useState, useEffect } from 'react';
import { Button } from '@/components/ui/button';
import { Card, CardContent } from '@/components/ui/card';
import axios from 'axios';

export default function CallPanel() {
  const [customers, setCustomers] = useState([]);
  const [currentCustomer, setCurrentCustomer] = useState(null);
  const [isCalling, setIsCalling] = useState(false);

  useEffect(() => {
    axios.get('/api/customers').then((res) => setCustomers(res.data));
  }, []);

  const startCall = async (customer) => {
    setIsCalling(true);
    setCurrentCustomer(customer);
    await axios.post('/api/call/start', { customer_id: customer.id });
  };

  return (
    <div className="p-4 grid grid-cols-1 md:grid-cols-2 gap-4">
      <Card>
        <CardContent>
          <h2 className="text-xl font-bold mb-2">顧客リスト</h2>
          <ul>
            {customers.map((cust) => (
              <li key={cust.id} className="mb-2">
                <div className="flex justify-between">
                  <span>{cust.name} ({cust.phone})</span>
                  <Button disabled={isCalling} onClick={() => startCall(cust)}>
                    発信
                  </Button>
                </div>
              </li>
            ))}
          </ul>
        </CardContent>
      </Card>

      {currentCustomer && (
        <Card>
          <CardContent>
            <h2 className="text-xl font-bold mb-2">通話中</h2>
            <p>{currentCustomer.name} に通話中...</p>
          </CardContent>
        </Card>
      )}
    </div>
  );
}
