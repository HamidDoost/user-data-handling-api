from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.db import get_async_session, init_db
from app.models.experiment_model import Experiment

router = APIRouter(
    prefix="/experiments",
    tags=["Experiment"],
    responses={404: {"description": "Not found"}},
)


@router.get("/experiments", response_model=list[Experiment])
async def get_experiments(session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(Experiment))
    experiments = result.scalars().all()
    return [
        Experiment(
            experiment_name=experiment.experiment_name,
            experiment_description=experiment.experiment_description,
            id=experiment.id,
        )
        for experiment in experiments
    ]


@router.post("/experiments")
async def add_experiment(
    experiment: Experiment, session: AsyncSession = Depends(get_async_session)
):
    experiment = Experiment(
        experiment_name=experiment.experiment_name,
        experiment_description=experiment.experiment_description,
        id=experiment.id,
    )
    session.add(experiment)
    await session.commit()
    await session.refresh(experiment)
    return experiment
