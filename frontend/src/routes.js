import { Route, Switch, Redirect } from "react-router-dom";
import { Home } from "./pages/Home";
import { Login } from "./pages/Login";
import { Signup } from "./pages/Signup";
import { OrderHistory } from "./pages/OrderHistory";
import { Search } from "./pages/Search";
import { Profile } from "./pages/Profile";

export const useRoutes = isAuthenticated => {
  if (isAuthenticated) {
    return (
      <Switch>
        <Route path={"/"} exact component={Home} />
        <Route path={"/history"} exact component={OrderHistory} />
        <Route path={"/search"} exact component={Search} />
        <Route path={"/profile"} exact component={Profile} />
        <Redirect to="/" />
      </Switch>
    );
  }

  return (
    <Switch>
      <Route path={"/login"} exact component={Login} />
      <Route path={"/signin"} exact component={Signup} />
      <Redirect to="/login" />
    </Switch>
  );
};