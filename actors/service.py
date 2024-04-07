from actors.repository import ActorRepository


class ActorService:
    def __init__(self) -> None:
        self.actor_repository = ActorRepository()

    def get_actors(self):
        return self.actor_repository.get_actors()

    def create_actor(self, name, bday, nationality):
        actor = dict(
            name=name,
            birthday=bday,
            nationality=nationality
        )

        return self.actor_repository.create_actor(actor=actor)
